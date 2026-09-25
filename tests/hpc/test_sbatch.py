from sequoia_toolkit.hpc.sbatch import SbatchOptions, render_sbatch_script


def test_render_minimal_script_contains_core_directives():
    options = SbatchOptions(job_name="mon_job", command="python train.py")
    script = render_sbatch_script(options)

    assert "#SBATCH --job-name=mon_job" in script
    assert "#SBATCH --partition=cpu" in script
    assert "python train.py" in script
    assert "--gres=gpu" not in script


def test_render_with_gpu_and_modules():
    options = SbatchOptions(
        job_name="entrainement_gpu",
        command="python train.py",
        partition="gpu",
        gpus=2,
        account="projet-xyz",
        modules=["cuda/12.2", "python/3.11"],
    )
    script = render_sbatch_script(options)

    assert "#SBATCH --gres=gpu:2" in script
    assert "#SBATCH --account=projet-xyz" in script
    assert "module load cuda/12.2" in script
    assert "module load python/3.11" in script
