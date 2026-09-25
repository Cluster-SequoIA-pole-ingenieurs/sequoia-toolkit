"""Resolution de chemins de donnees selon les conventions du cluster.

Beaucoup de clusters HPC exposent plusieurs espaces de stockage aux
caracteristiques differentes (rapide mais non sauvegarde / plus lent
mais perenne / home utilisateur limite en taille). Ce module centralise
la logique de "quel repertoire utiliser pour quoi", au lieu de la
dupliquer (et de la coder en dur differemment) dans chaque projet.

Les noms de variables d'environnement ci-dessous (SCRATCH, WORK) sont
des conventions courantes mais PAS necessairement celles du cluster
SequoIA : a verifier et adapter avec la documentation d'exploitation du
cluster (variables reellement exportees dans l'environnement de job).
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataPaths:
    """Regroupe les repertoires de donnees resolus pour un projet donne."""

    scratch: Path
    """Stockage rapide, generalement purge periodiquement : resultats intermediaires,
    caches, checkpoints frequents."""

    work: Path
    """Stockage perenne partage de l'equipe/projet : jeux de donnees, resultats a conserver."""

    home: Path
    """Repertoire personnel de l'utilisateur : configuration, petits scripts. A eviter
    pour des donnees volumineuses (quota generalement limite)."""

    def ensure_all(self) -> None:
        """Cree les trois repertoires (et leurs parents) s'ils n'existent pas."""
        for directory in (self.scratch, self.work, self.home):
            directory.mkdir(parents=True, exist_ok=True)


def resolve_data_paths(project_name: str) -> DataPaths:
    """Resout les repertoires scratch/work/home pour `project_name`.

    Lit les variables d'environnement `SCRATCH`, `WORK` et `HOME` si
    presentes ; sinon replie sur des sous-repertoires de `~/sequoia`
    (utile en developpement local, hors cluster).

    Args:
        project_name: nom court du projet, utilise comme sous-repertoire
            (ex: "detection-anomalies-ocean").
    """
    home = Path(os.environ.get("HOME", Path.home()))
    scratch_base = Path(os.environ.get("SCRATCH", home / "sequoia" / "scratch"))
    work_base = Path(os.environ.get("WORK", home / "sequoia" / "work"))

    return DataPaths(
        scratch=scratch_base / project_name,
        work=work_base / project_name,
        home=home / "sequoia" / project_name,
    )
