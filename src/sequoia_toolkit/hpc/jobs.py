"""Soumission et suivi de jobs Slurm (wrappers autour de sbatch/squeue/sacct).

Ces fonctions appellent des binaires externes via subprocess : elles ne
sont donc testables unitairement qu'en isolant l'appel systeme (voir
tests/test_jobs.py qui mocke `subprocess.run`). Sur une machine sans
Slurm (ex: CI GitHub Actions), ces fonctions ne peuvent pas s'executer
reellement — c'est attendu.
"""

from __future__ import annotations

import enum
import subprocess
import tempfile
import time
from pathlib import Path

from sequoia_toolkit.core.exceptions import SequoiaExternalToolError
from sequoia_toolkit.core.log import get_logger
from sequoia_toolkit.hpc.sbatch import SbatchOptions, render_sbatch_script

_log = get_logger(__name__)


class JobStatus(str, enum.Enum):
    """Sous-ensemble des etats Slurm utiles cote appelant Python."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    UNKNOWN = "UNKNOWN"


def submit_job(options: SbatchOptions, *, workdir: str | Path | None = None) -> str:
    """Genere le script sbatch, le soumet, et retourne le job id Slurm.

    Args:
        options: parametres du job (voir `SbatchOptions`).
        workdir: dossier ou ecrire le script genere. Par defaut, un
            dossier temporaire (le script reste utile pour audit/debug,
            donc en production preferer un dossier versionne du projet).

    Raises:
        SequoiaExternalToolError: si `sbatch` retourne un code d'erreur.
    """
    script_content = render_sbatch_script(options)

    target_dir = Path(workdir) if workdir else Path(tempfile.mkdtemp(prefix="sequoia-hpc-"))
    target_dir.mkdir(parents=True, exist_ok=True)
    script_path = target_dir / f"{options.job_name}.sbatch"
    script_path.write_text(script_content, encoding="utf-8")

    _log.info("Soumission du job '%s' via %s", options.job_name, script_path)
    result = subprocess.run(
        ["sbatch", "--parsable", str(script_path)],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        raise SequoiaExternalToolError(
            f"echec de sbatch pour {options.job_name} : {result.stderr.strip()}",
            exit_code=result.returncode,
        )

    job_id = result.stdout.strip().split(";")[0]
    _log.info("Job '%s' soumis avec l'id %s", options.job_name, job_id)
    return job_id


def get_job_status(job_id: str) -> JobStatus:
    """Interroge l'etat courant d'un job via `squeue` (puis `sacct` si termine)."""
    result = subprocess.run(
        ["squeue", "-j", job_id, "-h", "-o", "%T"],
        capture_output=True,
        text=True,
        check=False,
    )

    state = result.stdout.strip()
    if state:
        return _to_job_status(state)

    # Le job n'est plus dans la queue : il est termine, on consulte sacct.
    result = subprocess.run(
        ["sacct", "-j", job_id, "-n", "-o", "State", "--parsable2"],
        capture_output=True,
        text=True,
        check=False,
    )
    first_line = result.stdout.strip().splitlines()[0] if result.stdout.strip() else ""
    return _to_job_status(first_line)


def _to_job_status(raw_state: str) -> JobStatus:
    normalized = raw_state.split()[0].upper() if raw_state else ""
    try:
        return JobStatus(normalized)
    except ValueError:
        return JobStatus.UNKNOWN


def wait_for_job(job_id: str, *, poll_interval_seconds: float = 15.0) -> JobStatus:
    """Bloque jusqu'a ce que le job atteigne un etat terminal, puis le retourne.

    A utiliser depuis un notebook ou un script de pipeline, pas depuis un
    job Slurm lui-meme (eviter de bloquer une allocation de calcul en
    attente passive).
    """
    terminal_states = {
        JobStatus.COMPLETED,
        JobStatus.FAILED,
        JobStatus.CANCELLED,
        JobStatus.UNKNOWN,
    }
    while True:
        status = get_job_status(job_id)
        if status in terminal_states:
            return status
        time.sleep(poll_interval_seconds)
