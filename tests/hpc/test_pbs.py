import pytest

from sequoia_toolkit.core.exceptions import SequoiaExternalToolError
from sequoia_toolkit.hpc import JobSpec, JobStatus, PBSScheduler

PRO = PBSScheduler("pro")
TORQUE = PBSScheduler("torque")

SPEC = JobSpec(
    job_name="train",
    command="python train.py",
    queue="gpuq",
    nodes=2,
    ntasks_per_node=4,
    cpus_per_task=8,
    memory="64G",
    gpus=4,
    time_limit="48:00:00",
    account="proj42",
    extra_directives={"slurm": ["--constraint=a100"], "pbs": ["-l place=excl"]},
)

# Extraits de sorties reelles de "qstat -f" (attributs pertinents).
QSTAT_PRO_FINISHED = """Job Id: 1234.pbs-server
    Job_Name = train
    job_state = F
    queue = gpuq
    Exit_status = 0
"""
QSTAT_PRO_FAILED = QSTAT_PRO_FINISHED.replace("Exit_status = 0", "Exit_status = 271")
QSTAT_PRO_DELETED_WHILE_QUEUED = QSTAT_PRO_FINISHED.replace("    Exit_status = 0\n", "")
QSTAT_TORQUE_RUNNING = """Job Id: 99.torque-server
    Job_Name = train
    job_state = R
"""
QSTAT_TORQUE_COMPLETED = """Job Id: 99.torque-server
    job_state = C
    exit_status = 1
"""


def test_pro_header():
    script = PRO.render_script(SPEC)
    for line in [
        "#PBS -N train",
        "#PBS -S /bin/bash",
        "#PBS -q gpuq",
        "#PBS -l select=2:ncpus=32:mpiprocs=4:ngpus=4:mem=64gb",
        "#PBS -l walltime=48:00:00",
        "#PBS -o logs/",
        "#PBS -e logs/",
        "#PBS -A proj42",
        "#PBS -l place=excl",
    ]:
        assert line in script
    assert "constraint" not in script


def test_torque_header_uses_nodes_ppn_and_total_memory():
    script = TORQUE.render_script(SPEC)
    assert "#PBS -l nodes=2:ppn=32:gpus=4" in script
    assert "#PBS -l mem=128gb" in script  # 64G par noeud x 2 noeuds
    assert "select=" not in script


def test_body_returns_to_submit_dir_and_normalises_env():
    script = PRO.render_script(SPEC)
    assert 'cd "$PBS_O_WORKDIR"' in script
    assert 'export SEQUOIA_JOB_ID="$PBS_JOBID"' in script
    assert "export SEQUOIA_JOB_SCHEDULER=pbs" in script
    assert "export OMP_NUM_THREADS=8" in script
    assert "export SEQUOIA_JOB_SCHEDULER=torque" in TORQUE.render_script(SPEC)


def test_minimal_script_has_no_optional_directives():
    script = PRO.render_script(JobSpec(job_name="demo", command="x"))
    assert "-q " not in script
    assert "-A " not in script
    assert "ngpus" not in script


def test_submit_keeps_full_job_id(tmp_path, monkeypatch, runner):
    monkeypatch.chdir(tmp_path)
    runner.on("qsub", "1234.pbs-server\n")
    assert PRO.submit(JobSpec(job_name="demo", command="x"), workdir="jobs") == "1234.pbs-server"
    assert (tmp_path / "jobs/demo.pbs").is_file()
    assert (tmp_path / "logs").is_dir()


def test_submit_error_is_reported(tmp_path, monkeypatch, runner):
    monkeypatch.chdir(tmp_path)
    runner.on("qsub", "", returncode=38, stderr="qsub: Unknown queue")
    with pytest.raises(SequoiaExternalToolError, match="Unknown queue"):
        PRO.submit(JobSpec(job_name="demo", command="x"))


@pytest.mark.parametrize(
    ("output", "expected"),
    [
        (QSTAT_PRO_FINISHED, JobStatus.COMPLETED),
        (QSTAT_PRO_FAILED, JobStatus.FAILED),
        (QSTAT_PRO_DELETED_WHILE_QUEUED, JobStatus.CANCELLED),
        (QSTAT_PRO_FINISHED.replace("job_state = F", "job_state = Q"), JobStatus.PENDING),
        (QSTAT_PRO_FINISHED.replace("job_state = F", "job_state = H"), JobStatus.PENDING),
        (QSTAT_PRO_FINISHED.replace("job_state = F", "job_state = E"), JobStatus.RUNNING),
        (QSTAT_TORQUE_RUNNING, JobStatus.RUNNING),
        (QSTAT_TORQUE_COMPLETED, JobStatus.FAILED),
        ("", JobStatus.UNKNOWN),
    ],
)
def test_qstat_parsing(output, expected):
    assert PBSScheduler._parse_qstat_full(output) is expected


def test_pro_status_queries_history_torque_does_not(runner):
    runner.on("qstat", QSTAT_PRO_FINISHED)
    runner.on("qstat", QSTAT_TORQUE_RUNNING)
    assert PRO.status("1234.pbs-server") is JobStatus.COMPLETED
    assert TORQUE.status("99.torque-server") is JobStatus.RUNNING
    # Chez Torque, "-x" signifie sortie XML : il ne doit pas etre passe.
    assert runner.calls == [
        ["qstat", "-x", "-f", "1234.pbs-server"],
        ["qstat", "-f", "99.torque-server"],
    ]


def test_status_unknown_when_qstat_fails(runner):
    runner.on("qstat", "", returncode=153, stderr="qstat: Unknown Job Id")
    assert PRO.status("1") is JobStatus.UNKNOWN


def test_cancel(runner):
    runner.on("qdel")
    PRO.cancel("1234.pbs-server")
    assert runner.calls == [["qdel", "1234.pbs-server"]]


def test_unknown_flavor_rejected():
    with pytest.raises(ValueError, match="variante PBS inconnue"):
        PBSScheduler("lsf")  # type: ignore[arg-type]
