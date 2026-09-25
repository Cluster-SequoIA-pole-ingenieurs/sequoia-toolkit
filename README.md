# sequoia-toolkit

Boîte à outils réutilisable de l'équipe ingénierie du
[Cluster SequoIA](https://cluster-sequoia.univ-rennes.fr/) : un seul paquet
pour ne plus réécrire, projet après projet, les mêmes scripts de job (Slurm ou PBS), la même
gestion de configuration ou les mêmes utilitaires de données.

## Installation

```bash
# Installation de base (légère : seule dépendance, pyyaml)
pip install "sequoia-toolkit @ git+https://github.com/Cluster-SequoIA-pole-ingenieurs/sequoia-toolkit.git"

# Version figée (recommandé dans un projet de recherche, pour la reproductibilité)
pip install "sequoia-toolkit @ git+https://github.com/Cluster-SequoIA-pole-ingenieurs/sequoia-toolkit.git@v0.1.0"

# Avec les dépendances optionnelles d'un domaine
pip install "sequoia-toolkit[tracking] @ git+https://github.com/Cluster-SequoIA-pole-ingenieurs/sequoia-toolkit.git"
```

| Extra | Apporte | Pour qui |
|---|---|---|
| *(aucun)* | `core`, `hpc`, `data`, `ml` avec backend de logging simple | tout le monde |
| `tracking` | mlflow | projets qui suivent leurs expériences dans mlflow |
| `gpu` | (à définir, ex. torch) | entraînement sur GPU |
| `object-storage` | (à définir, ex. boto3) | stockage S3-compatible |
| `all` | tout ce qui précède | postes de développement |

## Ce qu'il y a dedans

| Module | Pour faire quoi | Fonctions principales |
|---|---|---|
| `sequoia_toolkit.core` | Socle commun | `get_logger`, `load_settings`, `retry`, `timeit`, `SequoiaError` |
| `sequoia_toolkit.hpc` | Jobs **Slurm et PBS** (Pro/OpenPBS, Torque) | `JobSpec`, `submit_job`, `wait_for_job`, `get_job_status`, `cancel_job`, `current_job` |
| `sequoia_toolkit.ml` | Suivi d'expériences | `start_run` |
| `sequoia_toolkit.data` | Données sur le cluster | `resolve_data_paths`, `verify_checksum`, `atomic_write` |

## En 20 lignes

```python
from sequoia_toolkit.core import get_logger, load_settings
from sequoia_toolkit.data import resolve_data_paths
from sequoia_toolkit.hpc import JobSpec, submit_job, wait_for_job
from sequoia_toolkit.ml import start_run

log = get_logger(__name__)
settings = load_settings()  # ./sequoia.yaml + variables SEQUOIA_*
paths = resolve_data_paths("mon-projet")  # scratch / work / home

# Même code sous Slurm et sous PBS : l'ordonnanceur est détecté automatiquement.
job_id = submit_job(
    JobSpec(
        job_name="entrainement",
        command="python train.py",
        queue="gpu",
        gpus=1,
        memory="32G",
        time_limit="04:00:00",
    )
)
log.info("Statut : %s", wait_for_job(job_id).value)

with start_run("baseline") as run:  # dans train.py
    run.log_param("lr", 1e-3)
    run.log_metric("val_accuracy", 0.87, step=10)
```

## En ligne de commande : un seul fichier de job pour Slurm et PBS

Plus besoin de maintenir un `.sbatch` et un `.pbs` : un `job.yaml` suffit
(modèle commenté : [`examples/job.yaml`](examples/job.yaml)).

```bash
sequoia-job detect                                  # slurm, pbs ou torque
sequoia-job render job.yaml                         # voir le script généré
sequoia-job --scheduler pbs render job.yaml         # ... pour un autre cluster
sequoia-job submit job.yaml --set gpus=2 --wait --timeout 3600
sequoia-job status <id>
sequoia-job cancel <id>
```

Correspondance détaillée des options et des états entre ordonnanceurs,
limites connues : [docs/hpc.md](docs/hpc.md).

Exemple Python complet et commenté : [`examples/entrainement.py`](examples/entrainement.py).
Configuration d'exemple : [`sequoia.yaml.example`](sequoia.yaml.example).

## ⚠️ À valider avec l'équipe infrastructure

- Noms des variables d'environnement de stockage (`SCRATCH`, `WORK`) utilisées
  par `resolve_data_paths` : conventions HPC courantes, pas forcément celles du cluster.
- Ordonnanceur(s) réellement utilisé(s) sur chaque cluster visé, et variante PBS (Pro/OpenPBS ou Torque).
- Noms des files/partitions et des modules à renseigner dans les `JobSpec` (aucune valeur imposée par défaut).
- Premier passage des tests d'intégration sur une machine PBS : `pytest -m integration --no-cov`.

## Contribuer

Ajouter une fonctionnalité = ajouter un fichier dans le bon sous-module.
Procédure en 5 étapes dans [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[EUPL-1.2](LICENSE) — European Union Public Licence, version 1.2.
