"""Logging structure et coherent pour tout le toolkit SequoIA.

Objectif : que deux equipes differentes qui utilisent sequoia-hpc et
sequoia-ml obtiennent des logs au meme format, avec le meme niveau
configurable via une seule variable d'environnement (SEQUOIA_LOG_LEVEL),
ce qui facilite le debogage sur les noeuds de calcul (logs souvent
recuperes a posteriori depuis un fichier slurm-*.out).
"""

from __future__ import annotations

import logging
import os
import sys
from functools import cache

_DEFAULT_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | job=%(sequoia_job_id)s | %(message)s"


class _JobIdFilter(logging.Filter):
    """Injecte l'identifiant de job Slurm (si present) dans chaque log."""

    def filter(self, record: logging.LogRecord) -> bool:
        record.sequoia_job_id = os.environ.get("SLURM_JOB_ID", "-")
        return True


@cache
def _configure_root() -> None:
    level_name = os.environ.get("SEQUOIA_LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(logging.Formatter(_DEFAULT_FORMAT))
    handler.addFilter(_JobIdFilter())

    root = logging.getLogger("sequoia")
    root.setLevel(level)
    root.addHandler(handler)
    root.propagate = False


def get_logger(name: str) -> logging.Logger:
    """Retourne un logger nomme, prefixe par 'sequoia.', configure une seule fois.

    Exemple:
        >>> from sequoia_toolkit.core.log import get_logger
        >>> log = get_logger(__name__)
        >>> log.info("Job soumis")
    """
    _configure_root()
    return logging.getLogger(f"sequoia.{name}")
