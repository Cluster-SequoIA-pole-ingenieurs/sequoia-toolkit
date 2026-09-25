"""Verification d'integrite de fichiers par somme de controle SHA-256.

Usage typique : verifier qu'un jeu de donnees copie sur le stockage
rapide du cluster (scratch) correspond bien au fichier source, avant de
lancer un entrainement dessus.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from sequoia_toolkit.core.exceptions import SequoiaError

_DEFAULT_CHUNK_SIZE = 1024 * 1024  # 1 Mo, adapte a un systeme de fichiers parallele


class SequoiaChecksumError(SequoiaError):
    """La somme de controle calculee ne correspond pas a celle attendue."""


def compute_sha256(path: str | Path, *, chunk_size: int = _DEFAULT_CHUNK_SIZE) -> str:
    """Calcule la somme SHA-256 d'un fichier, par lecture en flux (pas tout en memoire).

    Args:
        path: fichier a lire.
        chunk_size: taille des blocs de lecture, en octets.

    Raises:
        FileNotFoundError: si `path` n'existe pas.
    """
    file_path = Path(path)
    digest = hashlib.sha256()

    with file_path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)

    return digest.hexdigest()


def verify_checksum(path: str | Path, expected_sha256: str) -> None:
    """Verifie que le fichier `path` correspond a la somme SHA-256 attendue.

    Raises:
        SequoiaChecksumError: si la somme calculee differe de celle attendue.
        FileNotFoundError: si `path` n'existe pas.
    """
    actual = compute_sha256(path)
    if actual.lower() != expected_sha256.lower():
        raise SequoiaChecksumError(
            f"somme de controle invalide pour {path} : attendu {expected_sha256}, obtenu {actual}"
        )
