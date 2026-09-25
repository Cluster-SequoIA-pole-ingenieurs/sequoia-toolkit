"""Suivi d'experiences neutre vis-a-vis de l'outil de tracking sous-jacent.

Motivation : eviter que chaque equipe/projet du cluster couple son code
directement a mlflow OU wandb OU un simple fichier CSV. `ExperimentRun`
expose une API minimale (log_param, log_metric, log_artifact) ; le
backend reellement utilise est un detail d'implementation choisi a la
creation du run.

Backend par defaut : `LoggingBackend`, qui se contente d'ecrire dans les
logs sequoia_toolkit.core (utile en debut de projet, ou en CI). Un backend mlflow
pourra etre ajoute (`sequoia_toolkit.ml.backends.mlflow_backend`) sans changer le
code appelant, des que l'extra `tracking` est installe.
"""

from __future__ import annotations

import contextlib
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

from sequoia_toolkit.core.log import get_logger

_log = get_logger(__name__)


class TrackingBackend(Protocol):
    """Interface minimale qu'un backend de suivi d'experiences doit respecter."""

    def log_param(self, key: str, value: object) -> None: ...
    def log_metric(self, key: str, value: float, *, step: int | None = None) -> None: ...
    def log_artifact(self, path: str | Path) -> None: ...


@dataclass
class LoggingBackend:
    """Backend par defaut : ecrit simplement dans les logs sequoia_toolkit.core."""

    run_name: str

    def log_param(self, key: str, value: object) -> None:
        _log.info("[%s] param %s = %s", self.run_name, key, value)

    def log_metric(self, key: str, value: float, *, step: int | None = None) -> None:
        suffix = f" (step={step})" if step is not None else ""
        _log.info("[%s] metric %s = %s%s", self.run_name, key, value, suffix)

    def log_artifact(self, path: str | Path) -> None:
        _log.info("[%s] artefact enregistre : %s", self.run_name, path)


@dataclass
class ExperimentRun:
    """Represente une execution d'experience en cours.

    Enveloppe fine autour d'un `TrackingBackend` : le code metier ne
    manipule que cet objet, jamais directement mlflow/wandb.
    """

    name: str
    backend: TrackingBackend
    params: dict[str, object] = field(default_factory=dict)

    def log_param(self, key: str, value: object) -> None:
        self.params[key] = value
        self.backend.log_param(key, value)

    def log_metric(self, key: str, value: float, *, step: int | None = None) -> None:
        self.backend.log_metric(key, value, step=step)

    def log_artifact(self, path: str | Path) -> None:
        self.backend.log_artifact(path)


@contextlib.contextmanager
def start_run(name: str, *, backend: TrackingBackend | None = None) -> Iterator[ExperimentRun]:
    """Ouvre un run d'experience (gestionnaire de contexte).

    Exemple:
        >>> with start_run("baseline_resnet18") as run:
        ...     run.log_param("lr", 1e-3)
        ...     run.log_metric("val_accuracy", 0.87)
    """
    resolved_backend = backend or LoggingBackend(run_name=name)
    _log.info("Debut du run '%s'", name)
    run = ExperimentRun(name=name, backend=resolved_backend)
    try:
        yield run
    finally:
        _log.info("Fin du run '%s'", name)
