"""Chargement de configuration : fichier YAML + surcharge par variables d'env.

Convention retenue pour tout l'ecosysteme SequoIA : un fichier
`sequoia.yaml` (ou passe explicitement) fournit les valeurs par defaut ;
toute variable d'environnement prefixee `SEQUOIA_` surcharge la cle
correspondante (en minuscules, underscores). Cela permet de garder la
meme configuration versionnee dans un repo tout en l'adaptant facilement
par job Slurm (ex: SEQUOIA_DATA_DIR=/scratch/... sbatch job.sh).
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from sequoia_toolkit.core.exceptions import SequoiaConfigError

_ENV_PREFIX = "SEQUOIA_"
# Variables exportees par les scripts de job generes : informations sur le job,
# pas de la configuration (voir sequoia_toolkit.hpc.runtime).
_RESERVED_PREFIX = "SEQUOIA_JOB_"


@dataclass(frozen=True)
class Settings:
    """Conteneur de configuration generique.

    Attributs typiques utilises par les librairies du cluster ; a
    completer selon les besoins reels du projet (rester minimaliste ici,
    c'est le socle commun).
    """

    raw: dict[str, Any] = field(default_factory=dict)

    def get(self, key: str, default: Any = None) -> Any:
        return self.raw.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.raw[key]


def _apply_env_overrides(data: dict[str, Any]) -> dict[str, Any]:
    overridden = dict(data)
    for env_key, env_value in os.environ.items():
        if not env_key.startswith(_ENV_PREFIX) or env_key.startswith(_RESERVED_PREFIX):
            continue
        key = env_key[len(_ENV_PREFIX) :].lower()
        overridden[key] = env_value
    return overridden


def load_settings(path: str | Path | None = None) -> Settings:
    """Charge la configuration depuis un fichier YAML, puis applique les overrides d'env.

    Args:
        path: chemin vers un fichier YAML. Si None, cherche `./sequoia.yaml`
            puis retourne une configuration vide (overrides d'env seuls)
            si aucun fichier n'existe.

    Raises:
        SequoiaConfigError: si `path` est fourni explicitement mais introuvable,
            ou si le fichier n'est pas un YAML valide (mapping).
    """
    data: dict[str, Any] = {}

    candidate = Path(path) if path is not None else Path("sequoia.yaml")

    if candidate.exists():
        try:
            loaded = yaml.safe_load(candidate.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            raise SequoiaConfigError(f"YAML invalide dans {candidate}: {exc}") from exc

        if not isinstance(loaded, dict):
            raise SequoiaConfigError(
                f"Le fichier de configuration {candidate} doit contenir un mapping."
            )
        data = loaded
    elif path is not None:
        raise SequoiaConfigError(f"Fichier de configuration introuvable : {candidate}")

    return Settings(raw=_apply_env_overrides(data))
