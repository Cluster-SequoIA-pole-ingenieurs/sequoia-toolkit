# Projet SequoIA — à personnaliser

Décrire ici la capacité livrée, son utilisateur et un exemple minimal.
Le module `sequoia_project` est un squelette. Le test initial vérifie son
import depuis les sources.

## Développement

Prérequis : Git et [uv](https://docs.astral.sh/uv/getting-started/installation/).
Python 3.12 est le choix initial, à adapter à l'environnement scientifique visé.

```bash
uv sync
uv run --locked pre-commit install
uv run --locked pre-commit run --all-files
uv run --locked mypy
uv run --locked pytest -m 'not gpu and not integration and not slow' --cov
```

Versionner `uv.lock`, créé par `uv sync`. Les vérifications suivantes et la CI
utilisent `--locked` pour détecter une divergence entre manifeste et verrou.
Si un hook corrige un fichier, relire sa modification puis relancer la commande.

Ajouter le premier test de comportement dès le premier incrément fonctionnel.
Ne pas interpréter une CI verte sur le squelette comme une validation du projet.

Pytest trouve le code dans `src/` grâce à `pythonpath` dans `pyproject.toml`.
Pour lancer un module du projet depuis la racine avec Bash, utiliser par exemple
`PYTHONPATH=src uv run --locked python -m sequoia_project.mon_module` après avoir
créé `mon_module.py`.

## Tests spécifiques

Les marqueurs `gpu`, `integration` et `slow` sont déclarés mais exclus de la
commande CPU ci-dessus. Les marquer n'empêche pas leur exécution avec un simple
`pytest` ; utiliser explicitement la sélection appropriée.

Décrire ici les prérequis et commandes des tests scientifiques ou d'intégration
lorsqu'ils existent, et leurs conditions d'exécution. Les tests ordinaires ne
doivent télécharger ni modèles ni jeux de données, ni soumettre de jobs.

## Références à compléter

- Cadrage validé, critères d'acceptation et politique IA : référence approuvée.
- Données et modèles : modalités d'accès, licences et versions de référence.
- Responsable de maintenance et procédure de transfert.
- Licence du code : à convenir avant diffusion.

Créer l'AGENTS.md une fois le cadrage et la politique IA validés.
