"""sequoia_toolkit : boite a outils de l'equipe ingenierie du Cluster SequoIA.

Organisation en sous-modules, a importer explicitement :

- ``sequoia_toolkit.core`` : logging, configuration, exceptions, decorateurs
- ``sequoia_toolkit.hpc``  : generation / soumission / suivi de jobs Slurm
- ``sequoia_toolkit.ml``   : suivi d'experiences IA/ML
- ``sequoia_toolkit.data`` : chemins de donnees, checksums, ecriture atomique

Ce fichier n'importe volontairement aucun sous-module : ``import
sequoia_toolkit`` reste instantane, et les dependances optionnelles
(mlflow, torch, ...) ne sont chargees que par le sous-module qui en a besoin.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("sequoia-toolkit")
except PackageNotFoundError:
    __version__ = "0.0.0+dev"

__all__ = ["__version__"]
