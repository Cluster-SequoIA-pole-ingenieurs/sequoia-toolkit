"""Garde-fous de coherence de l'outillage du depot, executes en CI.

1. La version de ruff epinglee dans ``pyproject.toml`` est celle de
   ``.pre-commit-config.yaml`` : le lint est identique en local et en CI.
2. La version figee recommandee dans le README est la version courante du paquet.
"""

import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]


def _pyproject() -> str:
    return (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")


def _project_version() -> str:
    match = re.search(r'^version = "([^"]+)"$', _pyproject(), re.MULTILINE)
    assert match, "version introuvable dans pyproject.toml"
    return match.group(1)


def test_ruff_pin_matches_pre_commit():
    pinned = re.search(r'"ruff==([^"]+)"', _pyproject())
    assert pinned, "ruff doit etre epingle (ruff==X.Y.Z) dans les extras dev"

    config = yaml.safe_load((REPO_ROOT / ".pre-commit-config.yaml").read_text(encoding="utf-8"))
    revs = [r["rev"] for r in config["repos"] if r["repo"].endswith("/ruff-pre-commit")]
    assert revs == [f"v{pinned.group(1)}"], (
        "Versions de ruff divergentes entre pyproject.toml et .pre-commit-config.yaml"
    )


def test_readme_pins_current_version():
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    pinned_tags = set(re.findall(r"sequoia-toolkit\.git@(v[\w.]+)", readme))
    assert pinned_tags == {f"v{_project_version()}"}, (
        "Le README doit recommander la version courante (git tag vX.Y.Z)"
    )
