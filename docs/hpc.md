# Jobs HPC portables : Slurm et PBS

Un job est décrit **une seule fois** (`JobSpec` en Python, ou fichier `job.yaml`
pour la commande `sequoia-job`). Le toolkit le traduit pour l'ordonnanceur
du cluster : Slurm, PBS Pro / OpenPBS, ou Torque.

## Choix de l'ordonnanceur

Dans l'ordre :

1. paramètre explicite : `submit_job(spec, scheduler="pbs")` ou `sequoia-job --scheduler pbs ...` ;
2. variable `SEQUOIA_SCHEDULER=slurm|pbs|torque` (ou clé `scheduler` du `sequoia.yaml`, à passer à `get_scheduler`) ;
3. détection : `sbatch` présent → Slurm ; sinon `qsub` présent → PBS, la variante
   (Pro ou Torque) étant déduite de `qstat --version`.

Slurm est testé en premier, car certains sites Slurm fournissent des commandes
`qsub` de compatibilité. Imposer `SEQUOIA_SCHEDULER` sur un poste sans
ordonnanceur permet de **générer** des scripts (`sequoia-job render`) pour un autre cluster.

## Correspondance des champs

| `JobSpec` | Slurm | PBS Pro / OpenPBS | Torque |
|---|---|---|---|
| `job_name` | `--job-name` | `-N` | `-N` |
| `queue` | `--partition` | `-q` | `-q` |
| `nodes`, `ntasks_per_node`, `cpus_per_task` | `--nodes`, `--ntasks-per-node`, `--cpus-per-task` | `-l select=N:ncpus=T×C:mpiprocs=T` | `-l nodes=N:ppn=T×C` |
| `memory` (par nœud) | `--mem` | `:mem=` dans `select` (par nœud) | `-l mem=` (**total** = mémoire × nœuds) |
| `gpus` (par nœud) | `--gres=gpu:G` | `:ngpus=G` | `:gpus=G` |
| `time_limit` | `--time` | `-l walltime` | `-l walltime` |
| `account` | `--account` | `-A` | `-A` |
| `log_dir` | `--output/--error <dir>/%x-%j.out/.err` | `-o/-e <dir>/` (noms par défaut PBS) | idem |
| `extra_directives["slurm"]` / `["pbs"]` | ajoutées telles quelles, seulement pour la famille concernée | | |

Comportements harmonisés dans le script généré :

- **répertoire de travail** : Slurm démarre dans le répertoire de soumission,
  PBS dans `$HOME` → le script PBS fait `cd "$PBS_O_WORKDIR"` ;
- **shell** : bash imposé sous PBS (`-S /bin/bash`) ;
- **variables** : `SEQUOIA_JOB_ID`, `SEQUOIA_JOB_NAME`, `SEQUOIA_JOB_SCHEDULER`,
  `SEQUOIA_JOB_SUBMIT_DIR`, `SEQUOIA_JOB_NODES`, `SEQUOIA_JOB_CPUS_PER_TASK`,
  et `OMP_NUM_THREADS = cpus_per_task` (PBS Pro le fixerait sinon au nombre de cœurs du nœud) ;
- **robustesse** : `set -eo pipefail`, puis `set -u` après les `module load` ;
- **dossier de journaux** créé avant la soumission (ni Slurm ni PBS ne le créent,
  et les journaux sont alors perdus sans message).

Contraintes de portabilité vérifiées à la création du `JobSpec` : nom commençant
par une lettre (exigence PBS), durée au format `HH:MM:SS` (le format `J-HH:MM:SS`
n'existe que sous Slurm).

## États

| État normalisé | Slurm | PBS |
|---|---|---|
| `PENDING` | PENDING, CONFIGURING, REQUEUED, SUSPENDED… | Q, H, W, T, S |
| `RUNNING` | RUNNING, COMPLETING | R, E, B |
| `COMPLETED` | COMPLETED | F/C avec code retour 0 |
| `FAILED` | FAILED, TIMEOUT, OUT_OF_MEMORY, NODE_FAIL… | F/C avec code retour ≠ 0 |
| `CANCELLED` | CANCELLED | supprimé avant démarrage |
| `UNKNOWN` | job introuvable | job introuvable |

Sous PBS, un job tué en cours d'exécution (`qdel`, dépassement de walltime)
apparaît comme `FAILED` : PBS ne distingue pas ces cas dans son code retour.

Sous Slurm, l'état d'un job terminé est lu avec `sacct`, puis avec
`scontrol show job` si la comptabilité n'est pas activée sur le cluster.

## Dans le code exécuté par le job

```python
from sequoia_toolkit.hpc import current_job

job = current_job()  # None hors d'un job
workers = job.cpus_per_task if job and job.cpus_per_task else 1
```

## Limites actuelles

- Pas encore de tableaux de jobs (`--array` / `-J`) ni de dépendances entre jobs.
- Côté PBS, validé par tests unitaires (sorties `qsub`/`qstat` de référence,
  syntaxe bash) mais **pas encore sur un vrai serveur PBS** : lancer
  `pytest -m integration --no-cov` sur un nœud de connexion PBS au premier usage.

## Ajouter un ordonnanceur (OAR, LSF…)

1. Créer `src/sequoia_toolkit/hpc/schedulers/<nom>.py` avec une sous-classe de
   `Scheduler` : `header`, `runtime_exports`, `submit_args`, `parse_job_id`,
   `cancel_args`, `status`. Tout le reste est hérité.
2. L'enregistrer dans `_build` et `detect_scheduler` (`schedulers/__init__.py`).
3. Ajouter des tests sur le modèle de `tests/hpc/test_pbs.py`, puis ajouter son
   nom aux paramètres de `tests/hpc/test_script_syntax.py`.

Aucun code de projet n'est à modifier.
