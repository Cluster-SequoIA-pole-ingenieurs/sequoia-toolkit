import pytest

from sequoia_toolkit.data.atomic import atomic_write


def test_atomic_write_creates_final_file(tmp_path):
    target = tmp_path / "sous_dossier" / "resultat.txt"

    with atomic_write(target) as f:
        f.write("contenu final")

    assert target.read_text() == "contenu final"
    # aucun fichier temporaire ne doit trainer
    assert list(target.parent.iterdir()) == [target]


def _write_then_fail(target):
    with atomic_write(target) as f:
        f.write("contenu partiel")
        raise ValueError("echec simule pendant l'ecriture")


def test_atomic_write_does_not_leave_partial_file_on_error(tmp_path):
    target = tmp_path / "resultat.txt"

    with pytest.raises(ValueError, match="echec simule"):
        _write_then_fail(target)

    assert not target.exists()
    assert list(tmp_path.iterdir()) == []


def test_atomic_write_binary_mode(tmp_path):
    target = tmp_path / "donnees.bin"

    with atomic_write(target, mode="wb") as f:
        f.write(b"\x00\x01\x02")

    assert target.read_bytes() == b"\x00\x01\x02"
