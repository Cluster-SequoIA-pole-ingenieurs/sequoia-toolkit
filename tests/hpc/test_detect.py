import subprocess

import pytest

from sequoia_toolkit.core.exceptions import SequoiaConfigError, SequoiaExternalToolError
from sequoia_toolkit.hpc import PBSScheduler, SlurmScheduler, get_scheduler
from sequoia_toolkit.hpc import schedulers as sched_mod


def _which(*present):
    return lambda binary: f"/usr/bin/{binary}" if binary in present else None


def _qstat_version(text):
    return lambda *a, **k: subprocess.CompletedProcess(a[0], 0, text, "")


@pytest.fixture(autouse=True)
def _no_env(monkeypatch):
    monkeypatch.delenv("SEQUOIA_SCHEDULER", raising=False)


@pytest.mark.parametrize(
    ("name", "cls", "resolved"),
    [
        ("slurm", SlurmScheduler, "slurm"),
        ("PBS", PBSScheduler, "pbs"),
        ("openpbs", PBSScheduler, "pbs"),
        ("torque", PBSScheduler, "torque"),
    ],
)
def test_explicit_name(name, cls, resolved):
    scheduler = get_scheduler(name)
    assert isinstance(scheduler, cls) and scheduler.name == resolved


def test_unknown_name_rejected():
    with pytest.raises(SequoiaConfigError):
        get_scheduler("oar")


def test_env_variable_wins_over_detection(monkeypatch):
    monkeypatch.setattr(sched_mod.shutil, "which", _which("sbatch"))
    monkeypatch.setenv("SEQUOIA_SCHEDULER", "pbs")
    assert get_scheduler().name == "pbs"


def test_slurm_preferred_when_qsub_wrappers_exist(monkeypatch):
    monkeypatch.setattr(sched_mod.shutil, "which", _which("sbatch", "qsub"))
    assert get_scheduler().name == "slurm"


@pytest.mark.parametrize(
    ("version_output", "expected"),
    [("pbs_version = 2022.1.3\n", "pbs"), ("Version: 6.1.3\nCommit: abc\n", "torque")],
)
def test_pbs_flavor_detection(monkeypatch, version_output, expected):
    monkeypatch.setattr(sched_mod.shutil, "which", _which("qsub"))
    monkeypatch.setattr(sched_mod.subprocess, "run", _qstat_version(version_output))
    assert get_scheduler().name == expected


def test_no_scheduler_gives_actionable_error(monkeypatch):
    monkeypatch.setattr(sched_mod.shutil, "which", _which())
    with pytest.raises(SequoiaExternalToolError, match="SEQUOIA_SCHEDULER"):
        get_scheduler()
