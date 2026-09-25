"""Description d'un job, independante de l'ordonnanceur (Slurm, PBS, ...).

Un meme ``JobSpec`` est traduit en script sbatch ou qsub par l'adaptateur
de l'ordonnanceur (voir ``sequoia_toolkit.hpc.schedulers``). Le code des
projets ne manipule que cet objet : changer de cluster ne demande aucune
modification du code.

Les contraintes de validation sont volontairement l'intersection de ce
qu'acceptent Slurm et PBS, pour qu'un JobSpec valide soit soumissible
partout (ex: nom de job commencant par une lettre, duree en HH:MM:SS).
"""

from __future__ import annotations

import enum
import re
from dataclasses import dataclass, field, fields
from typing import Any

from sequoia_toolkit.core.exceptions import SequoiaConfigError

_JOB_NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]*$")
_TIME_RE = re.compile(r"^(\d+):([0-5]\d):([0-5]\d)$")
_MEMORY_RE = re.compile(r"^(\d+)\s*([KMGT])B?$", re.IGNORECASE)


class JobStatus(str, enum.Enum):
    """Etats normalises d'un job, communs a tous les ordonnanceurs."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    UNKNOWN = "UNKNOWN"

    @property
    def is_terminal(self) -> bool:
        return self in {
            JobStatus.COMPLETED,
            JobStatus.FAILED,
            JobStatus.CANCELLED,
            JobStatus.UNKNOWN,
        }


@dataclass(frozen=True)
class Memory:
    """Quantite de memoire, stockee sous forme (valeur, unite K/M/G/T)."""

    value: int
    unit: str

    @classmethod
    def parse(cls, text: str) -> Memory:
        match = _MEMORY_RE.match(text.strip())
        if not match:
            raise SequoiaConfigError(
                f"memoire invalide : {text!r} (formats acceptes : '500M', '16G', '1T')"
            )
        return cls(value=int(match.group(1)), unit=match.group(2).upper())

    def scaled(self, factor: int) -> Memory:
        return Memory(value=self.value * factor, unit=self.unit)


@dataclass
class JobSpec:
    """Ce que l'on veut executer, et avec quelles ressources.

    Attributes:
        job_name: nom du job (lettre initiale, puis lettres/chiffres/``_.-``).
        command: commande shell a executer (une ou plusieurs lignes).
        queue: partition Slurm / file PBS. ``None`` = file par defaut du site.
        nodes: nombre de noeuds.
        ntasks_per_node: nombre de taches (processus MPI) par noeud.
        cpus_per_task: coeurs par tache (exporte aussi en OMP_NUM_THREADS).
        memory: memoire PAR NOEUD, ex. ``"16G"``. ``None`` = defaut du site.
        gpus: GPU par noeud.
        time_limit: duree maximale, format ``HH:MM:SS`` (heures > 24 permises).
        log_dir: dossier des journaux stdout/stderr (cree a la soumission).
        account: compte / projet de calcul a debiter.
        modules: modules d'environnement a charger (``module load ...``).
        env: variables d'environnement a exporter dans le job.
        extra_directives: options propres a un ordonnanceur, sans prefixe,
            ex. ``{"slurm": ["--constraint=a100"], "pbs": ["-l place=excl"]}``.
            Seules celles de l'ordonnanceur utilise sont ecrites.
    """

    job_name: str
    command: str
    queue: str | None = None
    nodes: int = 1
    ntasks_per_node: int = 1
    cpus_per_task: int = 1
    memory: str | None = None
    gpus: int | None = None
    time_limit: str = "01:00:00"
    log_dir: str = "logs"
    account: str | None = None
    modules: list[str] = field(default_factory=list)
    env: dict[str, str] = field(default_factory=dict)
    extra_directives: dict[str, list[str]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not _JOB_NAME_RE.match(self.job_name):
            raise SequoiaConfigError(
                f"nom de job invalide : {self.job_name!r} (doit commencer par une "
                "lettre, puis lettres, chiffres, '_', '.' ou '-')"
            )
        if not self.command.strip():
            raise SequoiaConfigError("la commande du job est vide")
        for name in ("nodes", "ntasks_per_node", "cpus_per_task"):
            if getattr(self, name) < 1:
                raise SequoiaConfigError(f"{name} doit etre >= 1")
        if self.gpus is not None and self.gpus < 0:
            raise SequoiaConfigError("gpus doit etre >= 0")
        if not _TIME_RE.match(self.time_limit):
            raise SequoiaConfigError(
                f"time_limit invalide : {self.time_limit!r} (format attendu HH:MM:SS)"
            )
        if self.memory is not None:
            Memory.parse(self.memory)
        for key in self.env:
            if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", key):
                raise SequoiaConfigError(f"nom de variable d'environnement invalide : {key!r}")

    @property
    def memory_per_node(self) -> Memory | None:
        return Memory.parse(self.memory) if self.memory else None

    @property
    def cpus_per_node(self) -> int:
        return self.ntasks_per_node * self.cpus_per_task

    def directives_for(self, scheduler_family: str) -> list[str]:
        return list(self.extra_directives.get(scheduler_family, []))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> JobSpec:
        """Construit un JobSpec depuis un dictionnaire (ex: fichier YAML).

        Raises:
            SequoiaConfigError: cle inconnue ou valeur invalide.
        """
        known = {f.name for f in fields(cls)}
        unknown = set(data) - known
        if unknown:
            raise SequoiaConfigError(
                f"cles inconnues dans la description du job : {sorted(unknown)}"
            )
        try:
            return cls(**data)
        except TypeError as exc:
            raise SequoiaConfigError(f"description de job invalide : {exc}") from exc
