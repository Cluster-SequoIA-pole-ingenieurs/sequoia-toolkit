"""Les scripts generes doivent etre du bash valide, pour chaque ordonnanceur
(``bash -n`` : analyse syntaxique sans execution ; les directives sont des
commentaires pour bash)."""

import shutil
import subprocess

import pytest

from sequoia_toolkit.hpc import JobSpec, render_script

SPECS = [
    JobSpec(job_name="minimal", command="echo ok"),
    JobSpec(
        job_name="complet",
        command='python train.py --msg "a b"\necho "fin: $?"',
        queue="q",
        nodes=2,
        gpus=2,
        memory="8G",
        modules=["cuda/12.2"],
        env={"MESSAGE": "valeur avec espaces et 'quotes'"},
    ),
]


@pytest.mark.skipif(shutil.which("bash") is None, reason="bash absent")
@pytest.mark.parametrize("scheduler", ["slurm", "pbs", "torque"])
@pytest.mark.parametrize("spec", SPECS, ids=lambda s: s.job_name)
def test_generated_script_is_valid_bash(scheduler, spec):
    script = render_script(spec, scheduler=scheduler)
    result = subprocess.run(["bash", "-n"], input=script, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
