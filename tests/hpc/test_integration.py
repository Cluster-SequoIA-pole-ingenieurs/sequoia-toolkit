"""Tests d'integration sur un VRAI ordonnanceur.

Ignores automatiquement si aucun ordonnanceur n'est joignable (poste local,
CI standard). A lancer sur un noeud de connexion du cluster :

    pytest -m integration --no-cov              # ordonnanceur detecte
    SEQUOIA_TEST_QUEUE=debug pytest -m integration --no-cov   # file a utiliser

La CI GitHub les execute sous Slurm (job "integration-slurm").
"""

import os
import shutil

import pytest

from sequoia_toolkit.core.exceptions import SequoiaExternalToolError
from sequoia_toolkit.hpc import JobSpec, JobStatus, detect_scheduler, submit_job, wait_for_job

pytestmark = pytest.mark.integration


@pytest.fixture(scope="module")
def scheduler():
    try:
        detected = detect_scheduler()
    except SequoiaExternalToolError:
        pytest.skip("aucun ordonnanceur disponible")
    probe = "sinfo" if detected.family == "slurm" else "qstat"
    if shutil.which(probe) is None or detected._run([probe]).returncode != 0:
        pytest.skip(f"{detected.name} installe mais injoignable")
    return detected


def _spec(name, command):
    return JobSpec(
        job_name=name,
        command=command,
        queue=os.environ.get("SEQUOIA_TEST_QUEUE"),
        time_limit="00:05:00",
        log_dir="logs",
    )


def _wait(job_id, scheduler):
    return wait_for_job(job_id, scheduler=scheduler, poll_interval_seconds=1, timeout_seconds=300)


def test_successful_job(tmp_path, monkeypatch, scheduler):
    monkeypatch.chdir(tmp_path)
    command = 'echo "$SEQUOIA_JOB_ID" > result.txt\npwd >> result.txt'
    job_id = submit_job(_spec("okjob", command), scheduler=scheduler, workdir="jobs")
    assert _wait(job_id, scheduler) is JobStatus.COMPLETED

    written_id, workdir = (tmp_path / "result.txt").read_text().split()
    assert job_id.startswith(written_id) or written_id.startswith(job_id)
    assert workdir == str(tmp_path)  # meme repertoire de travail sous Slurm et PBS
    assert any((tmp_path / "logs").iterdir())


def test_failing_job(tmp_path, monkeypatch, scheduler):
    monkeypatch.chdir(tmp_path)
    job_id = submit_job(_spec("failjob", "exit 3"), scheduler=scheduler, workdir="jobs")
    assert _wait(job_id, scheduler) is JobStatus.FAILED


def test_unset_variable_fails_job(tmp_path, monkeypatch, scheduler):
    monkeypatch.chdir(tmp_path)
    job_id = submit_job(
        _spec("unsetvar", 'echo "$VARIABLE_INEXISTANTE"'), scheduler=scheduler, workdir="jobs"
    )
    assert _wait(job_id, scheduler) is JobStatus.FAILED  # set -u actif
