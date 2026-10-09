import pytest

from sequoia_toolkit.hpc import (
    JobSpec,
    JobStatus,
    SequoiaJobTimeoutError,
    SlurmScheduler,
    get_job_status,
    render_script,
    submit_job,
    wait_for_job,
)


def test_same_spec_renders_for_every_scheduler():
    spec = JobSpec(job_name="demo", command="echo ok", gpus=1)
    assert "#SBATCH --gres=gpu:1" in render_script(spec, scheduler="slurm")
    assert "ngpus=1" in render_script(spec, scheduler="pbs")
    assert "gpus=1" in render_script(spec, scheduler="torque")


def test_scheduler_from_environment(monkeypatch):
    monkeypatch.setenv("SEQUOIA_SCHEDULER", "torque")
    assert "#PBS -l nodes=1:ppn=1" in render_script(JobSpec(job_name="d", command="x"))


def test_submit_then_wait(tmp_path, monkeypatch, runner):
    monkeypatch.chdir(tmp_path)
    runner.on("qsub", "5.srv\n")
    runner.on("qstat", "job_state = R\n")
    runner.on("qstat", "job_state = F\nExit_status = 0\n")
    job_id = submit_job(JobSpec(job_name="d", command="x"), scheduler="pbs")
    assert wait_for_job(job_id, scheduler="pbs", poll_interval_seconds=0) is JobStatus.COMPLETED


def test_wait_timeout(runner):
    for _ in range(5):
        runner.on("squeue", "PENDING\n")
    with pytest.raises(SequoiaJobTimeoutError):
        wait_for_job("1", scheduler="slurm", poll_interval_seconds=0.01, timeout_seconds=0.02)


def test_get_job_status_accepts_scheduler_instance(runner):
    runner.on("squeue", "COMPLETING\n")
    assert get_job_status("1", scheduler=SlurmScheduler()) is JobStatus.RUNNING
