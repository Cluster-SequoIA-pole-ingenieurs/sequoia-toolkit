"""Soumission et suivi de jobs HPC, sous Slurm comme sous PBS (Pro/OpenPBS, Torque).

Un seul ``JobSpec`` decrit le job ; l'ordonnanceur est detecte automatiquement
(ou impose via ``SEQUOIA_SCHEDULER`` / le parametre ``scheduler``).
"""

from sequoia_toolkit.hpc.jobs import (
    SequoiaJobTimeoutError,
    cancel_job,
    get_job_status,
    render_script,
    submit_job,
    wait_for_job,
)
from sequoia_toolkit.hpc.runtime import JobContext, current_job
from sequoia_toolkit.hpc.schedulers import (
    PBSScheduler,
    Scheduler,
    SlurmScheduler,
    detect_scheduler,
    get_scheduler,
)
from sequoia_toolkit.hpc.spec import JobSpec, JobStatus

__all__ = [
    "JobSpec",
    "JobStatus",
    "render_script",
    "submit_job",
    "get_job_status",
    "wait_for_job",
    "cancel_job",
    "SequoiaJobTimeoutError",
    "current_job",
    "JobContext",
    "Scheduler",
    "SlurmScheduler",
    "PBSScheduler",
    "get_scheduler",
    "detect_scheduler",
]
