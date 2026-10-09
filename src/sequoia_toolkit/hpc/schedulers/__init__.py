"""Adaptateurs d'ordonnanceurs et selection de celui a utiliser.

Ordre de resolution de ``get_scheduler`` :

1. nom passe explicitement (``get_scheduler("pbs")``) ;
2. variable d'environnement ``SEQUOIA_SCHEDULER`` (ou cle ``scheduler`` du
   ``sequoia.yaml``, passee explicitement par l'appelant) ;
3. detection automatique : ``sbatch`` present -> Slurm ; sinon ``qsub`` present
   -> PBS, variante deduite de ``qstat --version``.

Slurm est teste en premier car certains sites Slurm installent des
commandes de compatibilite ``qsub``/``qstat`` qui tromperaient la detection.
"""

from __future__ import annotations

import os
import shutil
import subprocess

from sequoia_toolkit.core.exceptions import SequoiaConfigError, SequoiaExternalToolError
from sequoia_toolkit.hpc.schedulers.base import Scheduler
from sequoia_toolkit.hpc.schedulers.pbs import Flavor, PBSScheduler
from sequoia_toolkit.hpc.schedulers.slurm import SlurmScheduler

SUPPORTED = ("slurm", "pbs", "torque")


def _build(name: str) -> Scheduler:
    key = name.strip().lower()
    if key == "slurm":
        return SlurmScheduler()
    if key in ("pbs", "pbspro", "pbs-pro", "openpbs"):
        return PBSScheduler(flavor="pro")
    if key in ("torque", "pbs-torque"):
        return PBSScheduler(flavor="torque")
    raise SequoiaConfigError(f"ordonnanceur inconnu : {name!r} (valeurs acceptees : {SUPPORTED})")


def detect_pbs_flavor() -> Flavor:
    """PBS Pro / OpenPBS affichent 'pbs_version = ...', Torque 'Version: ...'."""
    try:
        # qstat est resolu via le PATH : son emplacement depend du site (modules).
        result = subprocess.run(
            ["qstat", "--version"],  # noqa: S607
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return "pro"
    text = (result.stdout + result.stderr).lower()
    if "pbs_version" in text:
        return "pro"
    if "torque" in text or text.strip().startswith("version:"):
        return "torque"
    return "pro"


def detect_scheduler() -> Scheduler:
    """Detecte l'ordonnanceur installe sur la machine courante."""
    if shutil.which("sbatch"):
        return SlurmScheduler()
    if shutil.which("qsub"):
        return PBSScheduler(flavor=detect_pbs_flavor())
    raise SequoiaExternalToolError(
        "aucun ordonnanceur detecte (ni sbatch ni qsub dans le PATH). Lancez depuis un "
        "noeud de connexion du cluster, ou definissez SEQUOIA_SCHEDULER=slurm|pbs|torque "
        "pour simplement generer les scripts."
    )


def get_scheduler(name: str | None = None) -> Scheduler:
    """Retourne l'adaptateur a utiliser (voir l'ordre de resolution du module)."""
    chosen = name or os.environ.get("SEQUOIA_SCHEDULER")
    return _build(chosen) if chosen else detect_scheduler()


__all__ = [
    "Scheduler",
    "SlurmScheduler",
    "PBSScheduler",
    "SUPPORTED",
    "get_scheduler",
    "detect_scheduler",
    "detect_pbs_flavor",
]
