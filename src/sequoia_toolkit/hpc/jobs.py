"""Facade simple : soumettre, suivre, attendre, annuler un job, quel que soit
l'ordonnanceur.

Chaque fonction accepte ``scheduler`` : un nom ("slurm", "pbs", "torque"), un
adaptateur deja construit, ou ``None`` pour la resolution automatique
(``SEQUOIA_SCHEDULER`` puis detection). Le code d'un projet n'a donc en general
jamais besoin de preciser l'ordonnanceur.
"""

from __future__ import annotations

import time
from pathlib import Path

from sequoia_toolkit.core.exceptions import SequoiaError
from sequoia_toolkit.hpc.schedulers import Scheduler, get_scheduler
from sequoia_toolkit.hpc.spec import JobSpec, JobStatus

SchedulerLike = Scheduler | str | None


class SequoiaJobTimeoutError(SequoiaError):
    """Le job n'a pas atteint d'etat final dans le delai imparti."""


def _resolve(scheduler: SchedulerLike) -> Scheduler:
    return scheduler if isinstance(scheduler, Scheduler) else get_scheduler(scheduler)


def render_script(spec: JobSpec, *, scheduler: SchedulerLike = None) -> str:
    """Texte du script de soumission (sbatch ou qsub), sans rien soumettre."""
    return _resolve(scheduler).render_script(spec)


def submit_job(
    spec: JobSpec, *, scheduler: SchedulerLike = None, workdir: str | Path | None = None
) -> str:
    """Soumet le job et retourne son identifiant.

    Args:
        spec: description du job.
        scheduler: voir la docstring du module.
        workdir: dossier ou conserver le script genere (conseille : un dossier
            du projet, pour garder une trace de ce qui a ete soumis).
    """
    return _resolve(scheduler).submit(spec, workdir=workdir)


def get_job_status(job_id: str, *, scheduler: SchedulerLike = None) -> JobStatus:
    return _resolve(scheduler).status(job_id)


def cancel_job(job_id: str, *, scheduler: SchedulerLike = None) -> None:
    _resolve(scheduler).cancel(job_id)


def wait_for_job(
    job_id: str,
    *,
    scheduler: SchedulerLike = None,
    poll_interval_seconds: float = 15.0,
    timeout_seconds: float | None = None,
) -> JobStatus:
    """Attend qu'un job atteigne un etat final, puis le retourne.

    A utiliser depuis un notebook ou un script de pipeline, pas depuis un job
    (ne pas immobiliser une allocation de calcul a attendre).

    Raises:
        SequoiaJobTimeoutError: si ``timeout_seconds`` est depasse.
    """
    resolved = _resolve(scheduler)
    deadline = None if timeout_seconds is None else time.monotonic() + timeout_seconds
    while True:
        status = resolved.status(job_id)
        if status.is_terminal:
            return status
        if deadline is not None and time.monotonic() >= deadline:
            raise SequoiaJobTimeoutError(
                f"le job {job_id} n'est pas termine apres {timeout_seconds}s "
                f"(etat : {status.value})"
            )
        time.sleep(poll_interval_seconds)
