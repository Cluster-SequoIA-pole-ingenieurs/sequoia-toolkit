"""Garde-fous d'architecture, executes en CI comme n'importe quel test.

1. ``core`` ne doit dependre d'aucun autre sous-module (c'est le socle).
2. Les sous-modules metier (hpc, ml, data) ne dependent pas les uns des
   autres : si un besoin commun apparait, il remonte dans ``core``.
3. ``import sequoia_toolkit`` ne charge aucun sous-module (import leger).
"""

import ast
import subprocess
import sys
from pathlib import Path

import pytest

PKG_ROOT = Path(__file__).resolve().parents[1] / "src" / "sequoia_toolkit"
SUBPACKAGES = ["core", "hpc", "ml", "data"]  # a completer si nouveau sous-module


def _imported_subpackages(subpackage: str) -> set[str]:
    found: set[str] = set()
    for py_file in (PKG_ROOT / subpackage).rglob("*.py"):
        tree = ast.parse(py_file.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            names: list[str] = []
            if isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module]
            elif isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            for name in names:
                parts = name.split(".")
                if parts[0] == "sequoia_toolkit" and len(parts) > 1:
                    found.add(parts[1])
    found.discard(subpackage)
    return found


def test_core_depends_on_no_other_subpackage():
    assert _imported_subpackages("core") == set()


@pytest.mark.parametrize("subpackage", [s for s in SUBPACKAGES if s != "core"])
def test_business_subpackages_only_depend_on_core(subpackage):
    assert _imported_subpackages(subpackage) <= {"core"}


def test_top_level_import_is_lightweight():
    code = (
        "import sys, sequoia_toolkit;"
        "loaded = [m for m in sys.modules if m.startswith('sequoia_toolkit.')];"
        "print(','.join(loaded))"
    )
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
    assert out.stdout.strip() == ""


def test_every_subpackage_is_declared():
    on_disk = {p.name for p in PKG_ROOT.iterdir() if (p / "__init__.py").exists()}
    assert on_disk == set(SUBPACKAGES)
