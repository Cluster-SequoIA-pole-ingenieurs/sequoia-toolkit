"""Informations sur le job courant, accessibles de la meme facon sous Slurm et PBS.

A utiliser DANS le code execute par un job, par exemple pour dimensionner
un DataLoader ou nommer un fichier de sortie :

    from sequoia_toolkit.hpc import current_job
    job = current_job()
    workers = job.cpus_per_task if job else 1

Les scripts generes par sequoia-toolkit exportent des variables normalisees
``SEQUOIA_JOB_*`` ; pour un job soumis a la main, on se rabat sur les
variables natives de Slurm ou de PBS.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class JobContext:
    scheduler: str
    job_id: str
    job_name: str | None
    submit_dir: str | None
    cpus_per_task: int | None
    array_index: int | None


def _int(value: str | None) -> int | None:
    try:
        return int(value) if value not in (None, "") else None
    except ValueError:
        return None


def current_job() -> JobContext | None:
    """Contexte du job en cours, ou ``None`` hors d'un job (poste local, login node)."""
    env = os.environ

    if env.get("SEQUOIA_JOB_ID"):
        scheduler = env.get("SEQUOIA_JOB_SCHEDULER", "unknown")
        array = (
            env.get("SLURM_ARRAY_TASK_ID") or env.get("PBS_ARRAY_INDEX") or env.get("PBS_ARRAYID")
        )
        return JobContext(
            scheduler=scheduler,
            job_id=env["SEQUOIA_JOB_ID"],
            job_name=env.get("SEQUOIA_JOB_NAME"),
            submit_dir=env.get("SEQUOIA_JOB_SUBMIT_DIR"),
            cpus_per_task=_int(env.get("SEQUOIA_JOB_CPUS_PER_TASK")),
            array_index=_int(array),
        )

    if env.get("SLURM_JOB_ID"):
        return JobContext(
            scheduler="slurm",
            job_id=env["SLURM_JOB_ID"],
            job_name=env.get("SLURM_JOB_NAME"),
            submit_dir=env.get("SLURM_SUBMIT_DIR"),
            cpus_per_task=_int(env.get("SLURM_CPUS_PER_TASK")),
            array_index=_int(env.get("SLURM_ARRAY_TASK_ID")),
        )

    if env.get("PBS_JOBID"):
        # PBS n'a pas de notion de "coeurs par tache" : NCPUS (Pro) ou PBS_NUM_PPN
        # (Torque) donnent les coeurs par noeud, valeur exacte pour 1 tache/noeud.
        return JobContext(
            scheduler="pbs",
            job_id=env["PBS_JOBID"],
            job_name=env.get("PBS_JOBNAME"),
            submit_dir=env.get("PBS_O_WORKDIR"),
            cpus_per_task=_int(env.get("NCPUS") or env.get("PBS_NUM_PPN")),
            array_index=_int(env.get("PBS_ARRAY_INDEX") or env.get("PBS_ARRAYID")),
        )

    return None
