# Changelog

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage : [SemVer](https://semver.org/lang/fr/).

## [Non publié]

## [0.2.0] - 2026-09-25

### Ajouté
- `hpc` : prise en charge de **PBS Pro / OpenPBS et Torque** en plus de Slurm,
  derrière une interface unique (`Scheduler`) ; détection automatique de
  l'ordonnanceur, ou choix via `SEQUOIA_SCHEDULER` / paramètre `scheduler`.
- `hpc` : `cancel_job`, `timeout_seconds` dans `wait_for_job`, `current_job()`
  (informations sur le job courant, identiques sous Slurm et PBS).
- `hpc` : champs `memory`, `env` et `extra_directives` dans la description de job.
- Commande `sequoia-job` (`detect`, `render`, `submit`, `status`, `cancel`) avec
  description de job en YAML, identique pour tous les ordonnanceurs.
- Tests d'intégration sur un vrai Slurm (`pytest -m integration`), exécutés en CI.

### Modifié (incompatible)
- `SbatchOptions` → `JobSpec` ; `render_sbatch_script(opts)` → `render_script(spec)`.
- Champ `partition` → `queue`, qui vaut désormais `None` par défaut (file du site)
  au lieu de `"cpu"`.
- `cpus_per_task` vaut 1 par défaut (au lieu de 4).
- `time_limit` doit être au format `HH:MM:SS` ; le nom du job doit commencer par une lettre.

### Corrigé
- Le dossier de journaux est créé avant la soumission (journaux perdus sinon).
- `set -u` activé après `module load` (certains systèmes de modules échouaient).
- Slurm : les états TIMEOUT, OUT_OF_MEMORY, NODE_FAIL… sont reconnus (`FAILED`
  au lieu de `UNKNOWN`) ; l'état d'un job terminé est lu même sans comptabilité.
- Journaux : l'identifiant de job PBS apparaît aussi dans les logs.

### Migration depuis 0.1.0

```python
# avant
from sequoia_toolkit.hpc import SbatchOptions, submit_job

submit_job(SbatchOptions(job_name="x", command="...", partition="gpu"))
# après
from sequoia_toolkit.hpc import JobSpec, submit_job

submit_job(JobSpec(job_name="x", command="...", queue="gpu"))
```

## [0.1.0] - 2026-09-25

### Ajouté
- `core` : logging (avec `SLURM_JOB_ID`), configuration YAML + variables `SEQUOIA_*`,
  exceptions communes, décorateurs `retry` / `timeit`.
- `hpc` : génération de scripts sbatch, soumission, suivi et attente de jobs Slurm.
- `ml` : suivi d'expériences neutre vis-à-vis du backend.
- `data` : chemins scratch/work/home, checksums SHA-256, écriture atomique.
