import pytest

from sequoia_toolkit.core.exceptions import SequoiaConfigError
from sequoia_toolkit.hpc import JobSpec, JobStatus
from sequoia_toolkit.hpc.spec import Memory


def test_defaults_are_valid():
    spec = JobSpec(job_name="demo", command="echo ok")
    assert spec.queue is None
    assert spec.cpus_per_node == 1


@pytest.mark.parametrize(
    "kwargs",
    [
        {"job_name": "1demo"},  # PBS exige une lettre initiale
        {"job_name": "mon job"},
        {"command": "   "},
        {"nodes": 0},
        {"cpus_per_task": 0},
        {"gpus": -1},
        {"time_limit": "1-00:00:00"},  # syntaxe Slurm seule, non portable
        {"time_limit": "10:61:00"},
        {"memory": "16 giga"},
        {"env": {"1VAR": "x"}},
    ],
)
def test_invalid_values_are_rejected(kwargs):
    base = {"job_name": "demo", "command": "echo ok"}
    with pytest.raises(SequoiaConfigError):
        JobSpec(**{**base, **kwargs})


def test_long_durations_are_allowed():
    JobSpec(job_name="demo", command="x", time_limit="72:00:00")


@pytest.mark.parametrize(
    ("text", "value", "unit"), [("16G", 16, "G"), ("500mb", 500, "M"), ("1 T", 1, "T")]
)
def test_memory_parsing(text, value, unit):
    assert Memory.parse(text) == Memory(value, unit)


def test_from_dict_rejects_unknown_keys():
    with pytest.raises(SequoiaConfigError, match="partition"):
        JobSpec.from_dict({"job_name": "demo", "command": "x", "partition": "gpu"})


def test_from_dict_builds_spec():
    spec = JobSpec.from_dict({"job_name": "demo", "command": "x", "gpus": 2})
    assert spec.gpus == 2


def test_terminal_states():
    assert JobStatus.COMPLETED.is_terminal
    assert JobStatus.UNKNOWN.is_terminal
    assert not JobStatus.PENDING.is_terminal
    assert not JobStatus.RUNNING.is_terminal
