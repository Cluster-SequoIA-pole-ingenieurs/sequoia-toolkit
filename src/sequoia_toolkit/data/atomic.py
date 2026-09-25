"""Ecriture atomique de fichiers sur systeme de fichiers partage.

Sur un systeme de fichiers parallele (Lustre, GPFS, ...) partage entre
plusieurs jobs, un lecteur concurrent peut lire un fichier pendant qu'il
est encore en cours d'ecriture. Le motif "ecrire dans un fichier
temporaire puis renommer" evite ce probleme : `os.rename` (ou
`Path.replace`) est atomique sur un meme systeme de fichiers.
"""

from __future__ import annotations

import contextlib
import os
import tempfile
from collections.abc import Iterator
from pathlib import Path
from typing import IO, Any


@contextlib.contextmanager
def atomic_write(
    path: str | Path, *, mode: str = "w", encoding: str | None = "utf-8"
) -> Iterator[IO[Any]]:
    """Ouvre un fichier temporaire, et le renomme vers `path` seulement en cas de succes.

    Exemple:
        >>> with atomic_write("resultats/metriques.json") as f:
        ...     f.write('{"accuracy": 0.87}')

    En cas d'exception dans le bloc `with`, le fichier temporaire est
    supprime et `path` n'est jamais modifie (pas d'ecriture partielle).

    Args:
        path: chemin final souhaite.
        mode: mode d'ouverture ("w" texte ou "wb" binaire).
        encoding: encodage, ignore si `mode` est binaire.
    """
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)

    is_binary = "b" in mode
    fd, tmp_name = tempfile.mkstemp(dir=target.parent, prefix=f".{target.name}.", suffix=".tmp")
    tmp_path = Path(tmp_name)

    try:
        with os.fdopen(fd, mode, encoding=None if is_binary else encoding) as handle:
            yield handle
        tmp_path.replace(target)
    except BaseException:
        tmp_path.unlink(missing_ok=True)
        raise
