from sequoia_toolkit.data.paths import resolve_data_paths


def test_resolve_data_paths_uses_env_vars(tmp_path, monkeypatch):
    monkeypatch.setenv("SCRATCH", str(tmp_path / "scratch"))
    monkeypatch.setenv("WORK", str(tmp_path / "work"))
    monkeypatch.setenv("HOME", str(tmp_path / "home"))

    paths = resolve_data_paths("mon-projet")

    assert paths.scratch == tmp_path / "scratch" / "mon-projet"
    assert paths.work == tmp_path / "work" / "mon-projet"
    assert paths.home == tmp_path / "home" / "sequoia" / "mon-projet"


def test_ensure_all_creates_directories(tmp_path, monkeypatch):
    monkeypatch.setenv("SCRATCH", str(tmp_path / "scratch"))
    monkeypatch.setenv("WORK", str(tmp_path / "work"))
    monkeypatch.setenv("HOME", str(tmp_path / "home"))

    paths = resolve_data_paths("mon-projet")
    paths.ensure_all()

    assert paths.scratch.is_dir()
    assert paths.work.is_dir()
    assert paths.home.is_dir()
