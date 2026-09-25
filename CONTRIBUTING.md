# Contribuer à sequoia-toolkit

## Démarrer

```bash
git clone https://github.com/Cluster-SequoIA-pole-ingenieurs/sequoia-toolkit.git
cd sequoia-toolkit
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
pytest
```

## Ajouter une fonctionnalité réutilisable (le cas le plus courant)

Le critère d'entrée est simple : **une fonction mérite d'entrer ici quand
elle a été (ou va être) utile dans au moins deux projets.** En dessous, elle
reste dans le projet.

1. **Choisir le sous-module** :
   - lié à Slurm / au calcul → `hpc/`
   - lié à l'entraînement / l'évaluation de modèles → `ml/`
   - lié à la lecture / écriture / au stockage de données → `data/`
   - générique et utile partout → `core/`
   - aucun ne convient → créer un nouveau sous-module (voir plus bas)
2. **Créer ou compléter un fichier** dans ce sous-module (ex. `hpc/arrays.py`),
   avec docstrings et annotations de type.
3. **Exposer la fonction** dans le `__init__.py` du sous-module (`__all__`).
4. **Ajouter les tests** dans `tests/<sous-module>/`. Les appels à des outils
   externes (sbatch, API réseau) sont mockés : la CI ne tourne pas sur le cluster.
5. **Noter le changement** dans la section « Non publié » de `CHANGELOG.md`,
   puis ouvrir une PR.

Si la fonctionnalité exige une dépendance lourde, l'ajouter dans un extra de
`pyproject.toml` (existant ou nouveau), **jamais** dans `dependencies`, et
l'importer à l'intérieur du sous-module concerné uniquement.

## Règles d'architecture (vérifiées automatiquement)

`tests/test_architecture.py` fait échouer la CI si :
- `core` importe un autre sous-module ;
- `hpc`, `ml` ou `data` s'importent entre eux (un besoin commun remonte dans `core`) ;
- `import sequoia_toolkit` charge un sous-module.

Ces règles gardent le paquet découpable : si un jour un sous-module doit vivre
dans son propre dépôt, il pourra en être extrait sans démêler de dépendances.

## Créer un nouveau sous-module

Créer `src/sequoia_toolkit/<nom>/__init__.py` et `tests/<nom>/__init__.py`,
puis ajouter `<nom>` à la liste `SUBPACKAGES` de `tests/test_architecture.py`
et une ligne `::: sequoia_toolkit.<nom>` dans `docs/api.md`.

## Conventions

- Branches : `feat/...`, `fix/...`, `docs/...`
- Commits : [Conventional Commits](https://www.conventionalcommits.org/fr/)
- Au moins une relecture avant fusion sur `main`
- Aucun secret ni identifiant dans le code

## Publier une version

1. Déplacer les entrées « Non publié » du `CHANGELOG.md` sous le nouveau numéro.
2. Mettre à jour `version` dans `pyproject.toml`.
3. `git tag vX.Y.Z && git push --tags` : la CI crée la GitHub Release.

Versionnage SemVer : changement incompatible de l'API publique → version majeure.
