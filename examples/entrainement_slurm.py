"""Exemple de bout en bout : configuration -> chemins -> job Slurm -> suivi.

A lancer depuis un noeud de connexion du cluster :
    python examples/entrainement_slurm.py
"""

from sequoia_toolkit.core import get_logger, load_settings
from sequoia_toolkit.data import resolve_data_paths
from sequoia_toolkit.hpc import SbatchOptions, submit_job, wait_for_job

log = get_logger(__name__)


def main() -> None:
    settings = load_settings()  # lit ./sequoia.yaml s'il existe, + variables SEQUOIA_*
    project = settings.get("project_name", "demo")

    paths = resolve_data_paths(project)
    paths.ensure_all()

    options = SbatchOptions(
        job_name=f"{project}-train",
        command=f"python train.py --data {paths.work} --out {paths.scratch}",
        partition=settings.get("partition", "gpu"),
        account=settings.get("account"),
        gpus=1,
        time_limit="04:00:00",
        log_dir=str(paths.scratch / "logs"),
    )

    job_id = submit_job(options, workdir=paths.scratch / "jobs")
    log.info("Job %s soumis, attente de la fin...", job_id)
    log.info("Statut final : %s", wait_for_job(job_id).value)


if __name__ == "__main__":
    main()
