"""Hierarchie d'exceptions commune a tout le toolkit SequoIA.

Chaque sous-module du toolkit (et les projets qui l'utilisent) devrait faire heriter ses exceptions
specifiques de `SequoiaError`, afin qu'un code appelant (ex: un pipeline
qui combine sequoia-hpc + sequoia-ml) puisse attraper une seule
famille d'erreurs si besoin.
"""

from __future__ import annotations


class SequoiaError(Exception):
    """Exception de base pour tout l'ecosysteme SequoIA."""


class SequoiaConfigError(SequoiaError):
    """Erreur de configuration (fichier manquant, cle invalide, ...)."""


class SequoiaExternalToolError(SequoiaError):
    """Erreur lors de l'appel a un outil externe (ex: Slurm, un registre de modeles)."""

    def __init__(self, message: str, *, exit_code: int | None = None) -> None:
        super().__init__(message)
        self.exit_code = exit_code
