from unittest.mock import patch

import pytest

from sequoia_toolkit.core.exceptions import SequoiaExternalToolError
from sequoia_toolkit.hpc.jobs import JobStatus, get_job_status, submit_job
from sequoia_toolkit.hpc.sbatch import SbatchOptions


class _FakeCompletedProcess:
    def __init__(self, returncode=0, stdout="", stderr=""):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def test_submit_job_returns_job_id(tmp_path):
    options = SbatchOptions(job_name="test_job", command="echo hello")

    with patch("subprocess.run", return_value=_FakeCompletedProcess(stdout="123456;cluster")):
        job_id = submit_job(options, workdir=tmp_path)

    assert job_id == "123456"
    assert (tmp_path / "test_job.sbatch").exists()


def test_submit_job_raises_on_sbatch_failure(tmp_path):
    options = SbatchOptions(job_name="test_job", command="echo hello")

    with (
        patch(
            "subprocess.run",
            return_value=_FakeCompletedProcess(returncode=1, stderr="partition invalide"),
        ),
        pytest.raises(SequoiaExternalToolError),
    ):
        submit_job(options, workdir=tmp_path)


def test_get_job_status_running_from_squeue():
    with patch("subprocess.run", return_value=_FakeCompletedProcess(stdout="RUNNING\n")):
        assert get_job_status("123") == JobStatus.RUNNING


def test_get_job_status_falls_back_to_sacct_when_not_in_queue():
    responses = [
        _FakeCompletedProcess(stdout=""),  # squeue : job absent de la queue
        _FakeCompletedProcess(stdout="COMPLETED\n"),  # sacct
    ]

    with patch("subprocess.run", side_effect=responses):
        assert get_job_status("123") == JobStatus.COMPLETED
