"""Exemple de bout en bout, identique sous Slurm et sous PBS.

A lancer depuis un noeud de connexion du cluster :
    python examples/entrainement.py

L'ordonnanceur est detecte automatiquement ; pour l'imposer :
    SEQUOIA_SCHEDULER=pbs python examples/entrainement.py
ou cle ``scheduler`` dans sequoia.yaml.
"""

from sequoia_toolkit.core import get_logger, load_settings
from sequoia_toolkit.data import resolve_data_paths
from sequoia_toolkit.hpc import JobSpec, get_scheduler, submit_job, wait_for_job

log = get_logger(__name__)


def main() -> None:
    settings = load_settings()  # ./sequoia.yaml + variables SEQUOIA_*
    project = settings.get("project_name", "demo")
    scheduler = get_scheduler(settings.get("scheduler"))  # None -> detection
    log.info("Ordonnanceur : %s", scheduler.name)

    paths = resolve_data_paths(project)
    paths.ensure_all()

    spec = JobSpec(
        job_name=f"{project}-train",
        command=f"python train.py --data {paths.work} --out {paths.scratch}",
        queue=settings.get("queue"),
        account=settings.get("account"),
        gpus=1,
        cpus_per_task=8,
        memory="32G",
        time_limit="04:00:00",
        log_dir=str(paths.scratch / "logs"),
    )

    job_id = submit_job(spec, scheduler=scheduler, workdir=paths.scratch / "jobs")
    log.info("Job %s soumis, attente de la fin...", job_id)
    log.info("Statut final : %s", wait_for_job(job_id, scheduler=scheduler).value)


if __name__ == "__main__":
    main()
