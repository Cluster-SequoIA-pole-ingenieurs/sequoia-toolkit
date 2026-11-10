# Skills — Guide d'utilisation

Ce répertoire contient les compétences (skills) pour agents IA de SequoIA. Chaque skill est un répertoire avec un fichier `SKILL.md`
standardisé [Agent Skills](https://agentskills.io/specification).

## Qu'est-ce qu'un skill ?

Un skill est un ensemble d'instructions spécialisées qu'un agent IA charge
à la demande pour accomplir un type de travail spécifique. Au lieu de noyer
l'agent dans des instructions permanentes, les agents qui supportent les skills
scanne les compétences disponibles et ne charge que celle qui correspond à la
tâche — ce qui économise l'espace contextuel et garde les réponses ciblées.

> Les skills de ce dépôt sont **indépendants de tout agent** : le même
> `SKILL.md` peut être utilisé avec Pi, Claude Code, ou tout autre agent qui
> implémente ce standard. Ce guide utilise **Pi** comme exemple principal
> car il est simple à installer et utiliser, mais les principes s'appliquent
> à tout agent compatible Agent Skills.

## Structure

```
skills/
├── sequoia-request-evaluator/
│   └── SKILL.md          # Instructions du skill
└── README.md             # Ce fichier
```

Chaque skill est un répertoire nommé contenant un `SKILL.md` avec un frontmatter
YAML descriptif :

```yaml
---
name: sequoia-request-evaluator
description: Evaluate SequoIA engineering support requests from academic
  researchers. Produces an internal critical assessment for engineering
  evaluators and a draft EasyChair XML review. Use when reviewing support
  submissions, feasibility assessments, or BurEx review forms.
---
```

Le champ `description` est la clé : c'est ce qui permet à l'agent de router la
bonne compétence. Il doit décrire à la fois le contenu du skill et le contexte
dans lequel il doit être utilisé.

## Skills disponibles

| Skill | Fichier | Pour quoi faire |
|---|---|---|
| `sequoia-request-evaluator` | `sequoia-request-evaluator/SKILL.md` | Évaluation de demandes de support ingénierie |

Pour les instructions détaillées d'un skill, lisez directement son `SKILL.md`.

## Installer Pi et configurer l'accès LLM

### 1. Installer Pi

```bash
curl -fsSL https://pi.dev/install.sh | sh
```

Vérifiez l'installation :

```bash
pi --version
```

Pi découvre les skills récursivement dans :

| Emplacement | Portée |
|---|---|
| `.pi/skills/` (projet) ou `.agents/skills/` | Ce dépôt et ses clones |
| `~/.pi/skills/` ou `~/.agents/skills/` | Global, tous les projets |

Le plus simple : démarrez Pi depuis la racine du dépôt, les skills dans
`skills/` seront découverts automatiquement (ce dossier est spécifié dans
`.pi/settings.json`).

### 2. Clé API ILaaS

[ILaaS](https://www.ilaas.fr/) (Intelligence Artificielle comme Service) est un service d'inférence souverain ouvert aux chercheurs de l'Enseignement Supérieur et de la Recherche français (ESR), hébergé par INRIA. Il fournit une API compatible OpenAI avec une large gamme de modèles open-source.

1. Rendez-vous sur la [page de demande de clés](https://www.ilaas.fr/demande-de-cles-individuelles-ilaas-esr/) et suivez les instructions pour obtenir une clé API personnelle (commence par `sk-`).
2. Stockez la clé dans `~/.pi/agent/auth.json` :

```json
{
  "ilaas": {
    "type": "api_key",
    "key": "sk-XXXXXXXXXXXXXXXXXXXXXXXX"
  }
}
```

### 3. Configurer le modèle

Configurez le modèle dans `~/.pi/agent/models.json` :

```json
{
  "providers": {
    "ilaas": {
      "baseUrl": "https://devllm.ilaas.fr/v1",
      "api": "openai-completions",
      "apiKey": "YOUR_ILAAS_API_KEY",
      "models": [
        {
          "id": "qwen-3.6-35b-instruct",
          "name": "Qwen 3.6 35B Instruct (ILaaS)",
          "api": "openai-completions",
          "reasoning": false,
          "contextWindow": 131072,
          "type": "chat"
        }
      ]
    }
  }
}
```

Le modèle recommandé pour les tâches de ce dépôt est `qwen-3.6-35b-instruct`.

### 4. Serveur MCP pdf-mcp (optionnel)

Pour lire des PDFs dans les skills, installez pdf-mcp :

```bash
pip install pdf-mcp
```

Ajoutez-le dans `~/.pi/agent/mcp.json` :

```json
{
  "mcpServers": {
    "pdf": {
      "command": "pdf-mcp"
    }
  }
}
```

Validez : `pi mcp list`

### 5. Invoquer un skill

```bash
cd /path/to/sequoia-toolkit
pi
```

Dans le chat, invoquez le skill soit **de manière déterministe** avec la commande
`/skill:name`, soit **en langage naturel** (Pi détectera automatiquement le
skill grâce à sa description) :

```
/skill:sequoia-request-evaluator
```

Puis fournissez le texte de la demande à évaluer. Les arguments après
`/skill:name` sont appendés aux instructions chargées.

Après modification d'un `SKILL.md`, rechargez l'agent avec :

```
/reload
```

### 6. Changer de modèle (facultatif)

Ajoutez d'autres modèles dans `models.json` et changez de modèle dans Pi avec `/model`.
Le skill fonctionne avec n'importe quel modèle de capacité suffisante
(contexte ≥ 32K recommandé).

## Exemple : évaluer une demande

Le workflow ci-dessous est celui utilisé par les ingénieurs SequoIA.
Supposez que les configurations ci-dessus (Pi, ILaaS, pdf-mcp) sont déjà en place.

1. **Invoquer le skill** dans le chat :
   ```
   /skill:sequoia-request-evaluator
   ```

2. **Indiquer le chemin du PDF** de soumission :
   ```
   Évaluez cette soumission : /path/to/soumission_12345.pdf
   ```

Le serveur pdf-mcp lira le PDF automatiquement ; l'agent extrait le texte
et l'analyse selon les instructions du skill.

**Recevez** :
- Section 1 : évaluation critique interne pour les ingénieurs
- Section 2 : proposition de remplissage du formulaire EasyChair

## Utiliser un skill avec d'autres agents

Puisque les skills suivent la spécification ouverte [Agent Skills](https://agentskills.io/specification),
ils sont portables au-delà de Pi :

| Agent | Comment utiliser un skill |
|---|---|
| **Pi** | Découverte automatique via `.agents/skills/`. Appeler un skill : `/skill:name` (déterministe) ou en langage naturel (Pi détecte le skill via sa `description`) |
| **Claude Code** | Placez `SKILL.md` dans `.agents/skills/` — Claude le détecte automatiquement |
| **Anthropic / OpenAI API** | Lisez `SKILL.md` et injectez le contenu comme prompt système |
| **Autres agents** | Le format est du Markdown + YAML frontmatter, lisible par tout LLM |

Le fichier `SKILL.md` ne contient aucune instruction spécifique à un agent —
c'est du Markdown standard avec des règles métier. N'importe quel agent peut
le consommer.

## Ajouter un nouveau skill

Pour ajouter une compétence dans le futur, depuis la racine du dépôt :

```bash
# 1. Créer le répertoire du skill
mkdir -p skills/mon-nouveau-skill

# 2. Écrire SKILL.md avec le frontmatter requis
cat > skills/mon-nouveau-skill/SKILL.md << 'EOF'
---
name: mon-nouveau-skill
description: Décrire ici ce que le skill fait ET quand l'utiliser. Ex : "Analyze
  Slurm job performance and generate reports. Use when profiling or optimizing
  HPC jobs."
---

# Mon Nouveau Skill

Instructions détaillées ici...
EOF
```

### Règles pour le frontmatter

| Champ | Règles |
|---|---|
| `name` | Minuscules, tirets, max 64 chars, pas de tirets consécutifs |
| `description` | Max 1024 chars. Dit **quoi** et **quand**. Exemple: 'Extract tables from PDFs. Use when you need to read tabular data from a PDF file.' Évitez les descriptions vagues comme 'Helps with PDFs. |
| `license` | Facultatif — nom ou fichier de licence |
| `metadata` | Facultatif — clés/valeurs supplémentaires |

### Arborescence optionnelle

```
skills/mon-nouveau-skill/
├── SKILL.md           # Instructions (requis)
├── scripts/           # Scripts exécutables (optionnel)
│   └── generate_report.py
├── references/        # Documentation de référence (optionnel)
│   └── slurm_limits.md
└── assets/            # Templates, formats (optionnel)
    └── rapport_template.yaml
```

### Tester

```bash
cd /path/to/sequoia-toolkit
pi
# soit /skill:mon-nouveau-skill (déterministe)
# soit en langage naturel : "Utilise le skill mon-nouveau-skill"
```
