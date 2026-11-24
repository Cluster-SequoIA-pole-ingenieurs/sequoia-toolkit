# Démarrer un projet Python avec le socle SequoIA

Ce guide accompagne le [squelette Python](python-project/). Il s'applique à un
nouveau dépôt GitHub ou GitLab. Pour un dépôt existant, intégrer les fichiers par une PR
en préservant son organisation et son environnement scientifique.

Le toolkit fournit ici des fichiers à copier : il n'est pas nécessaire
d'installer le paquet `sequoia-toolkit` pour utiliser les templates ou skills.
Les workflows placés dans `templates/` ne s'exécutent pas dans le toolkit.
Ils deviennent actifs après copie dans `.github/workflows/` du dépôt cible.

## 1. Choisir le dépôt et l'environnement

Confirmer avec l'équipe si le livrable prolonge un dépôt scientifique ou vit
dans un dépôt distinct.

Le squelette commence avec Python 3.12, un seul environnement CPU, Ruff,
Mypy, Pytest et uv. Avant de fixer Python, vérifier les versions compatibles
avec les dépendances scientifiques et l'environnement GPU cible. Pour un dépôt
existant, conserver le gestionnaire déjà utilisé s'il convient ; ne pas imposer
uv ou une migration complète pour ajouter la CI.

## 2. Copier dans un nouveau dépôt local vide

Installer Git et [uv](https://docs.astral.sh/uv/getting-started/installation/).
Partir d'une copie du squelette sans fichiers générés (`.venv/`, `uv.lock` ou
caches). L'exemple suppose que les deux dépôts sont voisins. Adapter les chemins
à votre machine et réserver la copie ci-dessous à un dépôt vide.

```bash
mkdir ../mon-projet
cp -R templates/python-project/. ../mon-projet/
cd ../mon-projet
git init -b main
```

Le `/.` copie aussi les fichiers cachés : `.github/`, `.gitignore`, etc.

Avant installation, personnaliser :

| Élément | Modification |
|---|---|
| `pyproject.toml` | Nom du projet, description et dépendances réelles |
| `src/sequoia_project/` | Renommer le paquet selon le livrable |
| Références à `sequoia_project` | Adapter la cible de couverture et le test d'import |
| Python | Garder `.python-version`, `requires-python`, Ruff et Mypy cohérents |
| `README.md` | Objectif, exemple, accès aux données, maintenance et licence convenue |

Le nom de distribution peut utiliser des tirets (`eosfm-benchmark`), celui du
paquet Python des underscores (`eosfm_benchmark`). Ce sont des exemples à
convenir, pas des noms imposés à EoS-FM.

## 3. Installer et lancer les vérifications

```bash
uv sync
git add .
uv run --locked pre-commit install
uv run --locked pre-commit run --all-files
uv run --locked mypy
uv run --locked pytest -m 'not gpu and not integration and not slow' --cov
```

`uv sync` crée l'environnement `.venv` et le verrou `uv.lock`. Relire les fichiers
stagés avant le premier commit, notamment pour exclure données et secrets.
Le premier lancement de pre-commit télécharge ses hooks. Si les hooks corrigent
des fichiers, relire, relancer puis stager les corrections avant de committer.
Le hook Git s'exécute ensuite à chaque commit ; la CI le relance indépendamment.

La CI échoue si `uv.lock` manque ou ne correspond plus à `pyproject.toml`.
Pour ajouter une dépendance, utiliser `uv add nom` (ou `uv add --dev nom`),
relire puis versionner le manifeste et le verrou ensemble.

Le seul test initial vérifie l'import depuis `src/`. Ajouter de vrais tests avant
de considérer une fonctionnalité livrée : chemins nominaux, erreurs et cas
limites, puis régression à chaque correction significative. La couverture est
mesurée sans seuil arbitraire ; convenir d'un seuil après les premiers tests.

## 4. Activer la CI et rendre les contrôles obligatoires

### Sur GitHub

Créer le dépôt distant avec la visibilité convenue, ajouter son URL comme
remote, puis pousser le premier commit selon la procédure de l'équipe.
Vérifier que GitHub Actions est autorisé et que le premier workflow passe.

Dans **Settings → Rules → Rulesets** (ou **Branches**, selon l'interface),
protéger la branche par défaut :

- Exiger une pull request et au moins une approbation humaine.
- Exiger les contrôles `Quality` et `CPU tests`, après leur premier run.
- Bloquer les force-push et la suppression de la branche ; limiter les bypass.

Vérifier les noms de contrôles réellement affichés par GitHub avant de les
sélectionner. Ces réglages ne sont pas activés par la simple copie des fichiers.
Leur disponibilité dépend de l'offre GitHub et de la visibilité du dépôt ;
si une option manque, voir avec l'administrateur et documenter la règle de revue.

Les jobs utilisent des runners GitHub hébergés, un jeton en lecture seule et
des actions épinglées par SHA. Ils n'ont besoin d'aucun secret de déploiement.
Dependabot propose chaque mois des mises à jour des dépendances et des actions.
Lors d'une mise à jour de uv, adapter les étapes d'installation dans la CI.
Le lock stabilise l'environnement de développement ; il ne prouve pas la
compatibilité d'une bibliothèque avec toutes les versions de ses dépendances.

Références : [verrouillage uv](https://docs.astral.sh/uv/concepts/projects/sync/),
[protection de branche GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

### Sur GitLab

Copier le [modèle GitLab CI](python-project-gitlab-ci.yml) à la racine du dépôt
cible sous le nom `.gitlab-ci.yml`. Utiliser un runner capable d'exécuter des
jobs dans une image conteneur. Adapter `image: python:3.12` si la version dans
`.python-version` change.

Les jobs `quality` et `cpu-tests` s'exécutent en parallèle pour les merge
requests, les pushes sur la branche par défaut et les pipelines lancés depuis
l'interface sur une branche. Le rapport JUnit affiche les résultats des tests
dans GitLab. Le typage est exécuté par `quality`, après pre-commit.

Protéger la branche par défaut et bloquer les pushes directs. Dans
**Settings → Merge requests → Merge checks**, activer **Pipelines must succeed**.
Configurer une approbation humaine si l'offre GitLab le permet. Pour réutiliser
le formulaire de PR, copier son contenu dans
`.gitlab/merge_request_templates/Default.md`.

[Déclenchement des pipelines](https://docs.gitlab.com/ci/yaml/workflow/) ·
[Contrôles avant fusion](https://docs.gitlab.com/user/project/merge_requests/auto_merge/#require-a-successful-pipeline-for-merge).

## 5. Construire un paquet si le projet doit être installé

Le socle exécute les contrôles directement depuis le dépôt. Pour une bibliothèque
ou un outil destiné à être installé, ajouter ces tables au `pyproject.toml`.
Placer `packaging` dans la table `[dependency-groups]` existante à côté de `dev`.

```toml
[build-system]
requires = ["hatchling>=1.27,<2"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/sequoia_project"]

[dependency-groups]
packaging = ["build>=1,<2", "hatchling>=1.27,<2", "twine>=7,<8"]
```

Adapter le nom du paquet et retirer `pythonpath = ["src"]` de la configuration
Pytest pour que les tests utilisent l'installation réalisée par `uv sync`.
Régénérer et versionner `uv.lock`. Copier le
[workflow de construction](python-project-package.yml) dans
`.github/workflows/package.yml` du projet et adapter son import final. Il valide
les distributions et installe la wheel dans un environnement vierge. Si la
distribution fait partie des livrables, rendre `Package` obligatoire après son
premier passage.
