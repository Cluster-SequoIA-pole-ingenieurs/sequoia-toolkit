import hashlib

import pytest

from sequoia_toolkit.data.checksums import SequoiaChecksumError, compute_sha256, verify_checksum


def test_compute_sha256_matches_known_value(tmp_path):
    file_path = tmp_path / "data.txt"
    file_path.write_text("sequoia")

    # Valeur de reference calculee independamment (hashlib, contenu "sequoia")
    expected = hashlib.sha256(b"sequoia").hexdigest()

    assert compute_sha256(file_path) == expected


def test_verify_checksum_passes_for_correct_hash(tmp_path):
    file_path = tmp_path / "data.txt"
    file_path.write_text("sequoia")
    correct_hash = compute_sha256(file_path)

    verify_checksum(file_path, correct_hash)  # ne doit pas lever


def test_verify_checksum_raises_for_incorrect_hash(tmp_path):
    file_path = tmp_path / "data.txt"
    file_path.write_text("sequoia")

    with pytest.raises(SequoiaChecksumError):
        verify_checksum(file_path, "0" * 64)


def test_compute_sha256_raises_for_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        compute_sha256(tmp_path / "absent.txt")
