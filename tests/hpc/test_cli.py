from pathlib import Path

from sequoia_toolkit.hpc.cli import main

JOB_YAML = """
job_name: demo
command: python train.py
gpus: 1
extra_directives:
  pbs: ["-l place=excl"]
"""


def _write(tmp_path, text=JOB_YAML):
    path = tmp_path / "job.yaml"
    path.write_text(text)
    return str(path)


def test_render_for_both_schedulers(tmp_path, capsys):
    path = _write(tmp_path)
    assert main(["--scheduler", "slurm", "render", path]) == 0
    assert "#SBATCH --gres=gpu:1" in capsys.readouterr().out
    assert main(["--scheduler", "pbs", "render", path]) == 0
    assert "#PBS -l place=excl" in capsys.readouterr().out


def test_set_overrides_with_typed_values(tmp_path, capsys):
    assert (
        main(
            [
                "--scheduler",
                "slurm",
                "render",
                _write(tmp_path),
                "--set",
                "gpus=4",
                "--set",
                "modules=[cuda/12.2]",
            ]
        )
        == 0
    )
    out = capsys.readouterr().out
    assert "--gres=gpu:4" in out
    assert "module load cuda/12.2" in out


def test_invalid_file_gives_clean_error(tmp_path, capsys):
    assert (
        main(["--scheduler", "slurm", "render", _write(tmp_path, "job_name: 1bad\ncommand: x\n")])
        == 2
    )
    assert "erreur" in capsys.readouterr().err


def test_submit_and_status(tmp_path, monkeypatch, capsys, runner):
    monkeypatch.chdir(tmp_path)
    runner.on("sbatch", "77\n")
    runner.on("squeue", "PENDING\n")
    assert main(["--scheduler", "slurm", "submit", _write(tmp_path)]) == 0
    assert main(["--scheduler", "slurm", "status", "77"]) == 0
    assert capsys.readouterr().out.split() == ["77", "PENDING"]
    assert (tmp_path / "jobs/demo.sbatch").is_file()


def test_detect(capsys):
    assert main(["--scheduler", "torque", "detect"]) == 0
    assert capsys.readouterr().out.strip() == "torque"


def test_shipped_example_is_valid(capsys):
    example = Path(__file__).resolve().parents[2] / "examples" / "job.yaml"
    for scheduler in ("slurm", "pbs", "torque"):
        assert main(["--scheduler", scheduler, "render", str(example)]) == 0
    capsys.readouterr()
