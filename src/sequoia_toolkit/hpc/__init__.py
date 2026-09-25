"""Generation, soumission et suivi de jobs Slurm.

Necessite les binaires Slurm (sbatch, squeue, sacct) dans le PATH,
c'est-a-dire une execution depuis un noeud de connexion du cluster.
"""

from sequoia_toolkit.hpc.jobs import JobStatus, get_job_status, submit_job, wait_for_job
from sequoia_toolkit.hpc.sbatch import SbatchOptions, render_sbatch_script

__all__ = [
    "SbatchOptions",
    "render_sbatch_script",
    "submit_job",
    "get_job_status",
    "wait_for_job",
    "JobStatus",
]
