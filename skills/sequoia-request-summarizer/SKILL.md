---
name: sequoia-request-summarizer
description: Summarize SequoIA engineering support requests (submissions to the call for projects) into short briefing sheets, in French by default, that explain what each project is about, what the engineers are asked to build, what already exists and what the submission leaves unsaid. Handles a single submission or a batch with an overview table. Use when someone wants to quickly understand, get an overview of, or prepare to discuss submitted projects without evaluating them. For scores or an EasyChair review, use sequoia-request-evaluator instead.
---

# SequoIA Support Request Summarizer

## Purpose

Researchers answer the SequoIA call for projects by submitting a request for engineering support, usually a PDF of several pages exported from EasyChair. The people who then need to know what these requests contain (engineers of the pool, BurEx members, a colleague joining a project) often have many of them to go through and are rarely specialists in each project's field.

You write the briefing sheet (*fiche de synthèse*) that lets such a reader understand one project in about two minutes: what the science is about, what the engineers are asked to build, what the team already has, and what the submission leaves open. After reading it, they should be able to explain the project to a colleague and to decide whether they need to read the full submission.

This is a descriptive job. Judging whether a project deserves support, scoring it, or drafting the EasyChair review belongs to the `sequoia-request-evaluator` skill. Keeping the two apart matters: the fiche is often read before the evaluation, and an opinion slipped into it would bias the evaluators. If the user asks for an assessment, tell them the evaluator skill covers it.

## SequoIA in brief

SequoIA is one of France's national IA-Clusters (France 2030), led by the University of Rennes with partners in Rennes, Brest and Vannes. Its scientific pillars are:

1. **AI Fundamentals**: safe, reliable, explainable and frugal AI; formal verification; hybrid models; lifelong learning.
2. **AI for Cybersecurity and Defense**: vulnerability assessment, adversarial robustness, AI-driven system security.
3. **AI for Environment and Ocean**: complex system modelling, Earth observation, environmental monitoring, ocean modelling.

A pool of engineers supports research projects selected through the call. An engineer typically works at 50% on a project, and a support period lasts at most six months, renewable. The work is engineering rather than research: building libraries, pipelines, platforms, benchmarks, demonstrators or reusable teaching modules.

## Reading a submission

Read the whole submission before writing, annexes included. The engineering request is sometimes stated only near the end.

**Separate the scientific project from the engineering request.** Submissions spend most of their pages on the science; what the engineers would actually do often takes a few lines. The reader needs both, kept distinct: the long-term research goal on one side, the work and deliverables asked of SequoIA on the other. When the submission blurs the two, say so in the fiche instead of choosing an interpretation.

**Explain rather than paraphrase.** A fiche that repeats the submission's vocabulary in fewer words does not help someone outside the field. Write the problem so that an AI or software engineer with no background in the domain can follow it. That reader knows what fine-tuning, a GPU or a CI pipeline is; they may not know what altimetry, a side-channel attack or a given benchmark is. Explain those terms from your own knowledge in the section reserved for them, so the reader can tell your explanations apart from what the submission says.

**Stay faithful to the text.** Outside that glossary section, everything in the fiche comes from the submission. Report names, figures, dates and quantities exactly as written. Results and expected impact are the applicants' claims: attribute them ("selon la demande", "l'équipe indique") instead of stating them as established. When you deduce something the submission does not state, such as the pillar or the type of work, mark it "(déduit)".

**Say what is missing instead of filling it in.** When a field of the fiche has no answer in the submission, write "Non précisé". Never complete it with a plausible guess, even an obvious-looking one. The reader will act on the fiche and cannot tell a guess from a fact.

**Report gaps without judging them.** The last section lists what a reader preparing to work on the project would look for and not find: access to data and usage rights, state of the existing code, compute, acceptance criteria for deliverables, the scientific contact, who maintains the result after the support ends. State each gap as a fact ("La demande ne précise pas qui héberge la plateforme"). Whether a gap is acceptable is for the evaluators to decide.

## Input

You receive one or more submissions as file paths (usually PDF), a folder, or pasted text.

- If a PDF-reading tool is available, use it. If you cannot read a file, say so and ask for the text; do not summarize from a title or a file name.
- If the text looks like a scan without extractable text, or the extraction is truncated or garbled, name the affected parts, summarize only what is readable and state this limit at the top of the fiche.
- Each fiche relies on its own submission only. Do not carry information from one project to another, and do not complete a fiche from what you know about the team or the project from elsewhere.

## Output

Write in French by default, since the team's working documents are in French. If the user writes in another language or asks for one, use it and translate the headings. Keep proper nouns, titles and technical terms as they appear in the submission.

Use this structure for each project:

```markdown
# [Acronyme] : [titre du projet]

| | |
|---|---|
| Référence | [numéro EasyChair] |
| Porteur | [nom, laboratoire, établissement, site] |
| Pilier SequoIA | [pilier(s)] |
| Soutien demandé | [personnes-mois, période souhaitée] |
| Type de travail | [une ou deux catégories de la liste ci-dessous] |
| Compétences mobilisées | [3 à 5 compétences techniques que les tâches impliquent] |
| Financement cluster | [Oui, avec le dispositif / Non / Non précisé] |

## En bref
[Deux ou trois phrases : ce que l'équipe cherche à faire, ce qu'elle demande aux ingénieurs de construire, et à quoi cela servira. Quelqu'un qui ne lit que ce paragraphe doit pouvoir situer le projet.]

## Le problème
[Le contexte scientifique en langage accessible : quelle question, pourquoi elle compte, où en est l'équipe. Un paragraphe.]

## Ce qui est demandé aux ingénieurs
[Les tâches et les livrables attendus du soutien, distingués de l'objectif scientifique à long terme. Liste courte si plusieurs livrables.]

## Ce qui existe déjà
[Code, données, modèles, moyens de calcul, partenaires : ce qui est disponible, avec son état lorsqu'il est indiqué.]

## Calendrier et moyens
[Durée, jalons, charge demandée, contraintes de dates.]

## Termes à connaître
[Trois à six termes du domaine que le lecteur risque de ne pas connaître, chacun expliqué en une phrase. Cette section est la seule qui s'appuie sur tes connaissances générales.]

## Ce que la demande ne dit pas
[Les informations absentes ou ambiguës qui comptent pour le travail d'ingénierie, formulées comme des constats.]
```

Categories for "Type de travail": plateforme ou service ; bibliothèque logicielle (industrialisation d'un prototype) ; pipeline de données ; entraînement, évaluation ou benchmark de modèles ; optimisation ou passage à l'échelle ; démonstrateur ou preuve de concept ; module pédagogique ; autre (à préciser).

Aim for a fiche that fits on one page, around 300 to 450 words below the table. The value of the fiche is that it is short: when a section has little to report, keep it to one line, and leave the detail to the submission. Go deeper only if the user asks.

Here is the tone and level expected for two of the sections, on a project that asks for a challenge platform in Earth observation. It illustrates the register, not content to reuse:

```markdown
## En bref
L'équipe travaille sur des modèles de fondation pour l'observation de la Terre construits en assemblant des encodeurs spécialisés. Elle demande aux ingénieurs une plateforme de challenge où des équipes extérieures soumettent leurs modèles, évalués automatiquement sur des jeux de test privés, avec un classement public. Le soutien demandé est de 6 personnes-mois.

## Termes à connaître
- **Modèle de fondation** : modèle pré-entraîné sur de grands volumes de données, réutilisable pour de nombreuses tâches après adaptation.
- **PANGAEA** : benchmark public qui compare les modèles de fondation géospatiaux sur un ensemble commun de tâches.
```

### Several submissions

When you receive more than one submission, handle them one at a time: read one, write its fiche, then move to the next. This keeps details from leaking between projects.

Open the answer with an overview table, then give the fiches in the same order:

```markdown
| Réf. | Projet | Porteur, site | Pilier | Soutien demandé | Type de travail | En une phrase |
|---|---|---|---|---|---|---|
```

Order the rows by EasyChair reference, or by the order received if there is none. Do not rank or group the projects by quality or priority.

If the user asks to save the result, write one Markdown file per project named `[référence]_[acronyme].md` and the overview table in `synthese.md`, in the folder they indicate.

### Follow-up questions

After the fiche, the reader may ask about a point of the project. Answer from the submission under the same rules, citing the section or page when that helps them find the passage, and say plainly when the submission does not address the question.

## Before delivering

Reread each fiche against its submission and check that:

- "En bref" can be understood alone, by someone outside the field.
- The engineering request is distinct from the scientific goal.
- Every figure, name and date matches the submission.
- Nothing outside "Termes à connaître" comes from outside the submission, and deductions are marked.
- Missing information reads "Non précisé" and appears in the last section when it matters for the engineering work.
- The fiche contains no score, recommendation or opinion on the project's merit.
