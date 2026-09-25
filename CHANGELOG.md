# Changelog

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage : [SemVer](https://semver.org/lang/fr/).

## [Non publié]

## [0.1.0] - 2026-09-25

### Ajouté
- `core` : logging (avec `SLURM_JOB_ID`), configuration YAML + variables `SEQUOIA_*`,
  exceptions communes, décorateurs `retry` / `timeit`.
- `hpc` : génération de scripts sbatch, soumission, suivi et attente de jobs Slurm.
- `ml` : suivi d'expériences neutre vis-à-vis du backend.
- `data` : chemins scratch/work/home, checksums SHA-256, écriture atomique.
