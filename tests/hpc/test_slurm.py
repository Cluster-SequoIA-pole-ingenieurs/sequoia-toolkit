from sequoia_toolkit.hpc import JobSpec, JobStatus, SlurmScheduler

SLURM = SlurmScheduler()


def _full_spec() -> JobSpec:
    return JobSpec(
        job_name="train",
        command="python train.py",
        queue="gpu",
        nodes=2,
        ntasks_per_node=4,
        cpus_per_task=8,
        memory="64G",
        gpus=4,
        time_limit="48:00:00",
        account="proj42",
        modules=["cuda/12.2"],
        env={"WANDB_MODE": "offline"},
        extra_directives={"slurm": ["--constraint=a100"], "pbs": ["-l place=excl"]},
    )


def test_render_full_header():
    script = SLURM.render_script(_full_spec())
    for line in [
        "#SBATCH --job-name=train",
        "#SBATCH --partition=gpu",
        "#SBATCH --nodes=2",
        "#SBATCH --ntasks-per-node=4",
        "#SBATCH --cpus-per-task=8",
        "#SBATCH --mem=64G",
        "#SBATCH --gres=gpu:4",
        "#SBATCH --time=48:00:00",
        "#SBATCH --output=logs/%x-%j.out",
        "#SBATCH --account=proj42",
        "#SBATCH --constraint=a100",
    ]:
        assert line in script
    assert "place=excl" not in script  # directive PBS ignoree sous Slurm


def test_render_body_is_normalised():
    script = SLURM.render_script(_full_spec())
    assert 'export SEQUOIA_JOB_ID="$SLURM_JOB_ID"' in script
    assert "export OMP_NUM_THREADS=8" in script
    assert "export WANDB_MODE=offline" in script
    assert script.index("module load cuda/12.2") < script.index("\nset -u\n")
    assert script.rstrip().endswith("python train.py")


def test_render_minimal_omits_optional_directives():
    script = SLURM.render_script(JobSpec(job_name="demo", command="echo ok"))
    for absent in ("--partition", "--mem", "--gres", "--account"):
        assert absent not in script


def test_submit_parses_id_and_creates_log_dir(tmp_path, monkeypatch, runner):
    monkeypatch.chdir(tmp_path)
    runner.on("sbatch", "4242;cluster\n")
    job_id = SLURM.submit(JobSpec(job_name="demo", command="x", log_dir="out/logs"), workdir="jobs")
    assert job_id == "4242"
    assert (tmp_path / "out/logs").is_dir()
    assert (tmp_path / "jobs/demo.sbatch").is_file()
    assert runner.calls[0][:2] == ["sbatch", "--parsable"]


def test_status_from_squeue(runner):
    runner.on("squeue", "RUNNING\n")
    assert SLURM.status("1") is JobStatus.RUNNING


def test_status_falls_back_to_sacct(runner):
    runner.on("squeue", "", returncode=1)
    runner.on("sacct", "CANCELLED by 1000\n")
    assert SLURM.status("1") is JobStatus.CANCELLED


def test_status_falls_back_to_scontrol_without_accounting(runner):
    runner.on("squeue", "")
    runner.on("sacct", "", returncode=1, stderr="accounting storage is disabled")
    runner.on("scontrol", "JobId=1 JobName=demo JobState=TIMEOUT Reason=TimeLimit")
    assert SLURM.status("1") is JobStatus.FAILED
    assert runner.binaries() == ["squeue", "sacct", "scontrol"]


def test_status_unknown_when_job_forgotten(runner):
    runner.on("squeue", "", returncode=1)
    runner.on("sacct", "")
    runner.on("scontrol", "", returncode=1)
    assert SLURM.status("1") is JobStatus.UNKNOWN


def test_cancel(runner):
    runner.on("scancel")
    SLURM.cancel("7")
    assert runner.calls == [["scancel", "7"]]
