"""Interface commune a tous les ordonnanceurs.

Tout ce qui ne depend pas de l'ordonnanceur est ecrit ici, une seule fois :
ecriture du script, soumission, gestion d'erreurs, corps du script (modules,
variables d'environnement, commande). Un adaptateur (Slurm, PBS, ...) ne
fournit que ce qui differe reellement : directives d'en-tete, commandes
de soumission/annulation, lecture de l'identifiant et de l'etat du job.

Ajouter un ordonnanceur (OAR, LSF, ...) = une nouvelle sous-classe, sans
toucher au code des projets.
"""

from __future__ import annotations

import shlex
import shutil
import subprocess
import tempfile
from abc import ABC, abstractmethod
from pathlib import Path
from typing import ClassVar

from sequoia_toolkit.core.exceptions import SequoiaExternalToolError
from sequoia_toolkit.core.log import get_logger
from sequoia_toolkit.hpc.spec import JobSpec, JobStatus

_log = get_logger(__name__)


class Scheduler(ABC):
    """Adaptateur d'un ordonnanceur de jobs."""

    #: identifiant court ("slurm", "pbs", "torque")
    name: str
    #: famille utilisee pour ``JobSpec.extra_directives`` ("slurm" ou "pbs")
    family: ClassVar[str]
    #: binaire de soumission, sert a la detection automatique
    submit_binary: ClassVar[str]
    #: extension des scripts generes
    script_suffix: ClassVar[str]

    # --- A fournir par chaque adaptateur -------------------------------

    @abstractmethod
    def header(self, spec: JobSpec) -> list[str]:
        """Lignes de directives (``#SBATCH ...`` / ``#PBS ...``)."""

    @abstractmethod
    def runtime_exports(self, spec: JobSpec) -> list[str]:
        """Lignes shell propres a l'ordonnanceur executees au debut du job
        (repertoire de travail, variables SEQUOIA_JOB_* normalisees)."""

    @abstractmethod
    def submit_args(self, script_path: Path) -> list[str]:
        """Commande de soumission du script."""

    @abstractmethod
    def parse_job_id(self, stdout: str) -> str:
        """Extrait l'identifiant du job de la sortie de soumission."""

    @abstractmethod
    def cancel_args(self, job_id: str) -> list[str]:
        """Commande d'annulation d'un job."""

    @abstractmethod
    def status(self, job_id: str) -> JobStatus:
        """Etat normalise du job."""

    # --- Commun a tous -------------------------------------------------

    @classmethod
    def is_available(cls) -> bool:
        return shutil.which(cls.submit_binary) is not None

    def render_script(self, spec: JobSpec) -> str:
        """Script complet, pret a etre soumis. Aucune entree/sortie."""
        lines = ["#!/bin/bash", *self.header(spec)]
        lines += [
            "",
            "# --- Genere par sequoia-toolkit : ne pas editer, modifier le JobSpec ---",
            "# 'set -u' n'est active qu'apres 'module load' : certains systemes de",
            "# modules referencent des variables non definies.",
            "set -eo pipefail",
            *self.runtime_exports(spec),
            f"export SEQUOIA_JOB_NAME={shlex.quote(spec.job_name)}",
            f"export SEQUOIA_JOB_NODES={spec.nodes}",
            f"export SEQUOIA_JOB_CPUS_PER_TASK={spec.cpus_per_task}",
            f"export OMP_NUM_THREADS={spec.cpus_per_task}",
        ]
        lines += [f"export {key}={shlex.quote(value)}" for key, value in spec.env.items()]
        lines += [f"module load {shlex.quote(module)}" for module in spec.modules]
        lines += ["set -u", "", spec.command.rstrip(), ""]
        return "\n".join(lines)

    def submit(self, spec: JobSpec, *, workdir: str | Path | None = None) -> str:
        """Ecrit le script, le soumet depuis le repertoire courant, retourne l'id.

        Le dossier de journaux est cree avant la soumission : ni Slurm ni PBS
        ne le creent, et un dossier absent fait perdre silencieusement les logs.
        """
        target_dir = Path(workdir) if workdir else Path(tempfile.mkdtemp(prefix="sequoia-hpc-"))
        target_dir.mkdir(parents=True, exist_ok=True)
        Path(spec.log_dir).mkdir(parents=True, exist_ok=True)

        script_path = target_dir / f"{spec.job_name}{self.script_suffix}"
        script_path.write_text(self.render_script(spec), encoding="utf-8")

        _log.info("Soumission de '%s' (%s) via %s", spec.job_name, self.name, script_path)
        result = self._run(self.submit_args(script_path))
        if result.returncode != 0:
            raise SequoiaExternalToolError(
                f"echec de la soumission {self.name} de '{spec.job_name}' : "
                f"{result.stderr.strip() or result.stdout.strip()}",
                exit_code=result.returncode,
            )
        job_id = self.parse_job_id(result.stdout)
        _log.info("Job '%s' soumis : %s", spec.job_name, job_id)
        return job_id

    def cancel(self, job_id: str) -> None:
        result = self._run(self.cancel_args(job_id))
        if result.returncode != 0:
            raise SequoiaExternalToolError(
                f"echec de l'annulation {self.name} du job {job_id} : {result.stderr.strip()}",
                exit_code=result.returncode,
            )
        _log.info("Job %s annule", job_id)

    @staticmethod
    def _run(args: list[str]) -> subprocess.CompletedProcess[str]:
        try:
            # args vient des methodes *_args de l'ordonnanceur, jamais d'un shell.
            return subprocess.run(args, capture_output=True, text=True, check=False)  # noqa: S603
        except FileNotFoundError as exc:
            raise SequoiaExternalToolError(
                f"commande introuvable : {args[0]} (etes-vous sur un noeud du cluster ?)"
            ) from exc
