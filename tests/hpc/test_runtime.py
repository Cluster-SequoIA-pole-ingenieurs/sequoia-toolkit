import pytest

from sequoia_toolkit.hpc import current_job

_ALL = [
    "SEQUOIA_JOB_ID",
    "SEQUOIA_JOB_SCHEDULER",
    "SEQUOIA_JOB_NAME",
    "SEQUOIA_JOB_SUBMIT_DIR",
    "SEQUOIA_JOB_CPUS_PER_TASK",
    "SLURM_JOB_ID",
    "SLURM_JOB_NAME",
    "SLURM_SUBMIT_DIR",
    "SLURM_CPUS_PER_TASK",
    "SLURM_ARRAY_TASK_ID",
    "PBS_JOBID",
    "PBS_JOBNAME",
    "PBS_O_WORKDIR",
    "NCPUS",
    "PBS_NUM_PPN",
    "PBS_ARRAY_INDEX",
    "PBS_ARRAYID",
]


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    for var in _ALL:
        monkeypatch.delenv(var, raising=False)


def test_outside_job():
    assert current_job() is None


def test_toolkit_variables_take_precedence(monkeypatch):
    monkeypatch.setenv("SEQUOIA_JOB_ID", "12.srv")
    monkeypatch.setenv("SEQUOIA_JOB_SCHEDULER", "pbs")
    monkeypatch.setenv("SEQUOIA_JOB_CPUS_PER_TASK", "8")
    monkeypatch.setenv("NCPUS", "32")  # coeurs par noeud, a ne pas confondre
    job = current_job()
    assert job is not None
    assert job.cpus_per_task == 8
    assert job.scheduler == "pbs"


def test_native_slurm(monkeypatch):
    monkeypatch.setenv("SLURM_JOB_ID", "7")
    monkeypatch.setenv("SLURM_CPUS_PER_TASK", "4")
    monkeypatch.setenv("SLURM_ARRAY_TASK_ID", "3")
    job = current_job()
    assert job is not None
    assert (job.scheduler, job.cpus_per_task, job.array_index) == ("slurm", 4, 3)


def test_native_torque(monkeypatch):
    monkeypatch.setenv("PBS_JOBID", "9.srv")
    monkeypatch.setenv("PBS_NUM_PPN", "16")
    monkeypatch.setenv("PBS_ARRAYID", "x")  # valeur invalide ignoree
    job = current_job()
    assert job is not None
    assert job.cpus_per_task == 16
    assert job.array_index is None
