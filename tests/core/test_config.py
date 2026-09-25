from sequoia_toolkit.core.config import load_settings


def test_load_settings_empty_when_no_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    settings = load_settings()
    assert settings.get("inexistant") is None


def test_load_settings_from_yaml(tmp_path):
    config_file = tmp_path / "conf.yaml"
    config_file.write_text("data_dir: /scratch/project\nbatch_size: 32\n")

    settings = load_settings(config_file)

    assert settings["data_dir"] == "/scratch/project"
    assert settings["batch_size"] == 32


def test_env_override_wins(tmp_path, monkeypatch):
    config_file = tmp_path / "conf.yaml"
    config_file.write_text("data_dir: /scratch/project\n")
    monkeypatch.setenv("SEQUOIA_DATA_DIR", "/scratch/override")

    settings = load_settings(config_file)

    assert settings["data_dir"] == "/scratch/override"


def test_job_variables_are_not_configuration(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("SEQUOIA_JOB_ID", "123")
    monkeypatch.setenv("SEQUOIA_SCHEDULER", "pbs")
    settings = load_settings()
    assert settings.get("job_id") is None
    assert settings.get("scheduler") == "pbs"
