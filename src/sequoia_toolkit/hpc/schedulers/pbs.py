"""Adaptateur PBS : PBS Pro / OpenPBS (``flavor="pro"``) et Torque (``flavor="torque"``).

Differences prises en charge entre les deux variantes :

- ressources : ``-l select=N:ncpus=..:mpiprocs=..`` (Pro) contre
  ``-l nodes=N:ppn=..`` (Torque) ; memoire par noeud (Pro) contre
  memoire totale du job (Torque) ;
- consultation d'un job termine : ``qstat -x -f`` (Pro ; ``-x`` = historique)
  contre ``qstat -f`` (Torque ; chez Torque ``-x`` signifie sortie XML !) ;
- etat final : ``F`` (Pro) contre ``C`` (Torque).

Differences avec Slurm compensees dans le script genere :

- PBS demarre le job dans ``$HOME`` : le script fait ``cd "$PBS_O_WORKDIR"``
  pour retrouver le comportement de Slurm (repertoire de soumission) ;
- PBS utilise sinon le shell de connexion de l'utilisateur : ``-S /bin/bash``.

Limite connue : les journaux prennent le nom par defaut de PBS
(``<job_name>.o<id>`` / ``.e<id>``) dans ``log_dir``, car PBS ne permet pas
d'utiliser l'identifiant du job dans le chemin des journaux.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Literal

from sequoia_toolkit.hpc.schedulers.base import Scheduler
from sequoia_toolkit.hpc.spec import JobSpec, JobStatus

Flavor = Literal["pro", "torque"]

_ACTIVE_STATES: dict[str, JobStatus] = {
    "Q": JobStatus.PENDING,  # en file
    "H": JobStatus.PENDING,  # retenu (hold)
    "W": JobStatus.PENDING,  # en attente d'une date de debut
    "T": JobStatus.PENDING,  # en transit
    "S": JobStatus.PENDING,  # suspendu
    "U": JobStatus.PENDING,  # suspendu (poste occupe)
    "M": JobStatus.PENDING,  # deplace vers un autre serveur
    "R": JobStatus.RUNNING,
    "E": JobStatus.RUNNING,  # en cours de terminaison
    "B": JobStatus.RUNNING,  # tableau de jobs demarre
}
_FINISHED_STATES = {"F", "C", "X"}
_ATTR_RE = re.compile(r"^\s*([A-Za-z_]+)\s*=\s*(.*?)\s*$")


def _memory_directive(value: int, unit: str) -> str:
    return f"{value}{unit.lower()}b"  # PBS : 16gb, 500mb


class PBSScheduler(Scheduler):
    family = "pbs"
    submit_binary = "qsub"
    script_suffix = ".pbs"

    def __init__(self, flavor: Flavor = "pro") -> None:
        if flavor not in ("pro", "torque"):
            raise ValueError(f"variante PBS inconnue : {flavor!r} (attendu 'pro' ou 'torque')")
        self.flavor: Flavor = flavor
        self.name = "pbs" if flavor == "pro" else "torque"

    def header(self, spec: JobSpec) -> list[str]:
        d = [f"-N {spec.job_name}", "-S /bin/bash"]
        if spec.queue:
            d.append(f"-q {spec.queue}")
        d += self._resources(spec)
        d += [
            f"-l walltime={spec.time_limit}",
            f"-o {spec.log_dir}/",
            f"-e {spec.log_dir}/",
        ]
        if spec.account:
            d.append(f"-A {spec.account}")
        d += spec.directives_for(self.family)
        return [f"#PBS {directive}" for directive in d]

    def _resources(self, spec: JobSpec) -> list[str]:
        memory = spec.memory_per_node
        if self.flavor == "pro":
            chunk = (
                f"select={spec.nodes}:ncpus={spec.cpus_per_node}:mpiprocs={spec.ntasks_per_node}"
            )
            if spec.gpus:
                chunk += f":ngpus={spec.gpus}"
            if memory:
                chunk += f":mem={_memory_directive(memory.value, memory.unit)}"
            return [f"-l {chunk}"]

        lines = [
            f"-l nodes={spec.nodes}:ppn={spec.cpus_per_node}"
            + (f":gpus={spec.gpus}" if spec.gpus else "")
        ]
        if memory:  # Torque : memoire totale du job
            total = memory.scaled(spec.nodes)
            lines.append(f"-l mem={_memory_directive(total.value, total.unit)}")
        return lines

    def runtime_exports(self, spec: JobSpec) -> list[str]:
        return [
            'cd "$PBS_O_WORKDIR"',
            f"export SEQUOIA_JOB_SCHEDULER={self.name}",
            'export SEQUOIA_JOB_ID="$PBS_JOBID"',
            'export SEQUOIA_JOB_SUBMIT_DIR="$PBS_O_WORKDIR"',
        ]

    def submit_args(self, script_path: Path) -> list[str]:
        return ["qsub", str(script_path)]

    def parse_job_id(self, stdout: str) -> str:
        # "12345.serveur" : l'identifiant complet est requis par qstat/qdel.
        return stdout.strip().splitlines()[-1].strip()

    def cancel_args(self, job_id: str) -> list[str]:
        return ["qdel", job_id]

    def status(self, job_id: str) -> JobStatus:
        args = ["qstat", "-x", "-f", job_id] if self.flavor == "pro" else ["qstat", "-f", job_id]
        result = self._run(args)
        if result.returncode != 0:
            return JobStatus.UNKNOWN
        return self._parse_qstat_full(result.stdout)

    @staticmethod
    def _parse_qstat_full(output: str) -> JobStatus:
        attrs: dict[str, str] = {}
        for line in output.splitlines():
            match = _ATTR_RE.match(line)
            if match:
                attrs.setdefault(match.group(1).lower(), match.group(2))

        state = attrs.get("job_state", "").upper()
        if state in _ACTIVE_STATES:
            return _ACTIVE_STATES[state]
        if state in _FINISHED_STATES:
            exit_status = attrs.get("exit_status")
            if exit_status is None:
                return JobStatus.CANCELLED  # supprime avant d'avoir demarre
            try:
                code = int(exit_status)
            except ValueError:
                return JobStatus.UNKNOWN
            # code >= 256 : tue par un signal (qdel, depassement de walltime...) ;
            # PBS ne distingue pas les deux, on renvoie FAILED dans les deux cas.
            return JobStatus.COMPLETED if code == 0 else JobStatus.FAILED
        return JobStatus.UNKNOWN
