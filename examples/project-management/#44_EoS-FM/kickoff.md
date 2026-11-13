# SequoIA — Réunion de lancement d'un soutien d'ingénierie — EoS-FM Challenge

> **Document unique de cadrage, vivant** · Prérempli avant la réunion, modifié collectivement pendant le kick-off et validé ensuite.
> **Durée indicative :** 60–90 min · **Statut :** `Préparation` · **Dernière mise à jour :** 12/11/2026.
> **Convention :** `☐` à cocher ; compléter les champs `[entre crochets]`. **`[Demande]`** = information présente dans la proposition EasyChair #44 ; **`[Proposition]`** = hypothèse de cadrage non validée ; **`[À décider]`** = question ouverte ; **`[Validé – date]`** = accord explicite.
> **Mode d’emploi :** avant la réunion, préremplir les sections 0–6 à partir de la demande EasyChair #44, en distinguant informations établies, propositions et points à décider. Pendant le kick-off, **modifier directement les sections concernées** pour refléter le cadrage convenu. Consigner en **section 7 les actions à réaliser**, avec leur responsable, leurs éventuels contributeurs et leur échéance, puis créer ou renseigner les tickets Jira correspondants. Après la réunion, finaliser le document et faire valider le cadrage en **section 8**.

## 0. Identification

| Champ | Valeur |
|---|---|
| Projet / acronyme | **EoS-FM Challenge: Community-built Ensembles of Specialists for Earth Observation** |
| Référence de la demande EasyChair | **#44** |
| Date du kick-off | [JJ/MM/AAAA — à fixer] |
| Porteur / référent scientifique | **Sébastien Lefèvre**, IRISA (UMR 6074), Université Bretagne Sud, Vannes — sebastien.lefevre@irisa.fr |
| Ingénieurs SequoIA | Clément Sage (référent), Nouhaila Aitbella |
| Autres contributeurs | **Minh-Tan Pham et Pierre Adorni** (équipe scientifique IRISA/UBS) ; **ESA Φ-lab**, collaboration envisagée, apport technique non confirmé |
| Période de soutien envisagée | Démarrage flexible, dès disponibilité des ressources ; **lancement visé dans les six mois** suivant le début du soutien `[Demande]` ; dates exactes [À décider] |
| Liens de travail | [Jira / dépôt de la plateforme / espace documentaire à créer] ; code scientifique : https://github.com/pierreadorni/EoS-FM ; article : https://arxiv.org/abs/2511.21523 |

**Participants :** Sébastien, Nouhaila, Clément
**Personnes absentes à consulter :** [À renseigner ; notamment référents hébergement/SSI/ESA selon décisions]

## 1. Contexte scientifique et résultats recherchés (10 min)

**Problème scientifique / métier :**
`[Demande]` Les modèles de fondation en observation de la Terre doivent transférer leurs représentations entre tâches, capteurs et régions. EoS-FM explore une approche modulaire associant des encodeurs spécialistes entraînés sur des jeux de données et tâches différents. Une étude de référence porte sur **22 spécialistes évalués sur 11 tâches PANGAEA**.

**Objectif du projet à plus long terme :**
`[Demande]` Organiser un **challenge international** dans lequel des équipes soumettent des collections de modèles spécialistes. Un protocole commun et des **jeux de test privés** permettront de comparer les contributions, de mieux comprendre leur complémentarité et de favoriser l'émergence d'un modèle géospatial de référence. Le protocole, les contraintes de soumission et les métriques restent à établir avec l'équipe scientifique et les partenaires éventuels.

**Résultat attendu du soutien SequoIA :**
`[Demande]` Concevoir, développer et déployer une **plateforme de challenge** intégrant le code EoS-FM : soumission et gestion des contributions, exécution isolée, orchestration d'évaluations, protection des jeux privés, suivi des résultats, **leaderboard public**, documentation et pilote complet.

**Lien avec les axes de SequoIA :**
`[Proposition]` Contribution aux travaux sur les fondations de l'IA (ensembles de modèles spécialistes, évaluation robuste) et aux applications en observation de la Terre / environnement. La demande mentionne un soutien du cluster via la **chaire PANORAMIX**, ainsi que CNES, UBS et ANR DREAMS autour du projet scientifique.

## 2. Périmètre, livrables et critères de réussite (15 min)

### 2.1 Livrables d'ingénierie

| ID | Livrable concret | Critère d'acceptation vérifiable | Validation par |
|---|---|---|---|
| L1 | **Plateforme de challenge déployable** : interface de soumission, gestion des évaluations et leaderboard public `[Demande]` | `[Proposition]` Une soumission conforme est enregistrée, évaluée, puis son résultat admissible est affiché sur le leaderboard ; statut et erreurs consultables | [Référent scientifique + responsable plateforme, à confirmer] |
| L2 | **Pipeline EoS-FM intégré**, tâches privées sélectionnées et résultats reproductibles `[Demande]` | `[Proposition]` Une contribution de référence est évaluée de bout en bout selon un protocole documenté, avec résultats reproductibles et sans exposition des données privées aux participants | [Équipe scientifique, à désigner] |
| L3 | **Interface de soumission et documentation** pour participants et organisateurs `[Demande]` | `[Proposition]` Un participant pilote réalise une soumission avec le guide ; un organisateur suit une procédure documentée d'installation/exploitation | [Référent scientifique + futur exploitant, à désigner] |
| L4 | **Pilote de bout en bout**, plateforme prête pour la préparation du lancement `[Demande]` | `[Proposition]` Un test pilote avec des soumissions représentatives est exécuté ; limites, incidents et conditions restantes pour l'ouverture sont documentés | [Référent scientifique + responsable hébergement/SSI, à désigner] |

**MVP — résultat indispensable à la fin du soutien :**
`[Proposition]` Plateforme pilote fonctionnelle sur un **ensemble limité de tâches**, avec **format de soumission contraint**, exécution isolée validée pour ce format, évaluation reproductible, leaderboard minimal et documentation. **Le niveau d'ouverture attendu à six mois** (pilote fermé, accès sur invitation ou ouverture publique) est `[À décider]` ; il ne faut pas substituer silencieusement un pilote fermé au lancement visé dans la demande.

**Dans le périmètre :**
- `[Demande]` Définition d'une interface de soumission et étude de l'architecture d'exécution/sécurité.
- `[Demande]` Workflow de soumission et gestion des participants ; orchestration, droits d'accès et limites de ressources.
- `[Demande]` Adaptation/intégration des modèles et du pipeline EoS-FM pour les tâches retenues ; protection des données privées ; reproductibilité.
- `[Demande]` Leaderboard, administration, tests, documentation, pilote et préparation au lancement.

**Hors périmètre initial (évolutions possibles) :**
- `[Proposition]` Prendre en charge sans limite tous les frameworks, dépendances et codes arbitraires de participants.
- `[Proposition]` Garantir une maintenance/exploitation indéfinie de la plateforme après les six personnes-mois de soutien.

**Hypothèses structurantes :** `[À décider]` Format des soumissions (poids seuls, API normalisée, conteneurs ou code libre) ; tâches et métriques du challenge ; possibilité ou non d'entraînement/adaptation pendant l'évaluation ; nombre de participants et quotas ; disponibilité des données privées ; accès aux GPU et environnement autorisant l'exécution isolée ; contribution d'ESA Φ-lab.

## 3. État de l'existant et prérequis (10 min)

| Élément | État actuel / emplacement | Responsable de l'accès | Prêt ? |
|---|---|---|---|
| Code, prototypes, modèles | `[Demande]` Dépôt EoS-FM et spécialistes préentraînés : https://github.com/pierreadorni/EoS-FM ; maturité, dépendances et reproductibilité à auditer | Équipe scientifique IRISA [contact à préciser] | ☐ Oui ☐ Non ☒ À vérifier |
| Données et annotations | `[Demande]` Jeux publics utilisés pour les travaux EoS-FM ; jeux supplémentaires non publiés évoqués par Φ-lab, **sans accord de disponibilité ou de droits à ce stade** | Équipe scientifique / interlocuteur Φ-lab [à désigner] | ☐ Oui ☐ Non ☒ À vérifier |
| Infrastructure et calcul | `[Demande]` Accès passé à **IDRIS Jean Zay** pour la recherche ; **UBS ou ESA** envisagés pour la plateforme ; hébergeur et ressources non choisis | [Référents UBS/ESA à désigner] | ☐ Oui ☐ Non ☒ À vérifier |
| Jeux de test / validation | `[Demande]` Évaluation scientifique publiée sur PANGAEA ; tâches privées, accès et protocole du challenge à définir | Équipe scientifique / Φ-lab [à préciser] | ☐ Oui ☐ Non ☒ À vérifier |
| Documentation et licences | `[Demande]` Article : https://arxiv.org/abs/2511.21523 ; code disponible ; licences des éléments intégrés, droits sur les soumissions et données privées à examiner | Équipe scientifique / services compétents [à préciser] | ☐ Oui ☐ Non ☒ À vérifier |

### 3.1 Prérequis de démarrage vs dépendances à lever plus tard

> Le tableau ci-dessous propose des **phases de besoin**, pas une décision sur leur caractère bloquant. À arbitrer avec les responsables pendant le kick-off.

| Élément à obtenir / décision | Nécessaire avant… | Statut | Responsable | Date cible / solution transitoire |
|---|---|---|---|---|
| Accès opérationnel au dépôt et exécution de référence EoS-FM | ☒ Démarrage ☐ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Équipe scientifique + ingénieurs [référents à préciser] | [Date] ; audit initial du dépôt public |
| Protocole pilote et format minimal de soumission | ☐ Démarrage ☒ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Référent scientifique + ingénieurs | [Date] ; interface temporaire sur modèles de référence |
| Jeux privés, droits d'utilisation et modalités d'accès | ☐ Démarrage ☐ Intégration ☒ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Équipe scientifique / Φ-lab [personne à confirmer] | [Date] ; données publiques ou synthétiques pour le développement, **pas comme substitut à la validation finale** |
| Environnement GPU pour tests et évaluations | ☐ Démarrage ☒ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Hébergeur / ingénieurs [à désigner] | [Date] ; plateforme de développement transitoire si autorisée |
| Hébergement de production, isolation des soumissions, validation SSI et quotas | ☐ Démarrage ☐ Intégration ☒ Pilote ☒ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Hébergeur UBS/ESA et service SSI [à désigner] | [Date] ; simulation de soumissions de confiance tant que non validé |
| Exploitant et moyens de fonctionnement après le soutien | ☐ Démarrage ☐ Intégration ☐ Pilote ☒ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Porteur / hébergeur [à désigner] | [Date] ; définir périmètre du transfert |

**Conditions minimales d'engagement de l'ingénieur :** `[À décider]` Proposition : accès au dépôt et interlocuteurs scientifiques disponibles ; un **démarrage exploratoire limité** (audit, architecture, tests sur code de confiance et données publiques/synthétiques) pourrait être envisagé sans données privées ni hébergement définitif.
**Conditions à satisfaire avant pilote / ouverture externe :** `[Proposition]` Format/protocole établis ; autorisations d'utilisation des données ; environnement et isolation validés par l'hébergeur/SSI ; quotas, accès et journaux testés ; responsabilités d'exploitation attribuées.
**Décision de démarrage :** ☐ Go ☐ Go limité (activités autorisées : [à définir]) ☐ No-go, en attente de [à définir]. **`[À décider]`**

## 4. Utilisation d'assistants IA pour le développement (10 min)

> **La demande EasyChair ne mentionne aucune autorisation d'utiliser des assistants IA.** Les questions suivantes concernent les outils de développement des ingénieurs, distincts des modèles participants au challenge. L'accord scientifique ne dispense pas des validations institutionnelles ou contractuelles.

### 4.1 Accord de principe du porteur

**Le porteur souhaite-t-il autoriser les ingénieurs à utiliser des assistants IA pour ce soutien ?**
☐ Oui, sous réserve des restrictions ci-dessous
☐ Non
☒ À confirmer

**Usages envisagés :**
☐ Aide à la rédaction de code  ☐ Refactorisation  ☐ Génération de tests  ☐ Débogage
☐ Documentation  ☐ Revue de code  ☐ Analyse de données / logs  ☐ Autre : [Préciser]

**Usages ou composants explicitement interdits :** `[À décider]`

### 4.2 Classification et contraintes des informations

**Le travail comporte-t-il des éléments soumis à des restrictions particulières ?**
☐ Aucun identifié  ☐ Code ou résultats non publiés  ☐ Données personnelles
☐ Données confidentielles de partenaires / industrielles  ☐ Secret contractuel ou propriété intellectuelle sensible
☐ Données ou technologies soumises à des restrictions réglementaires / de sécurité  ☐ Autre : [Préciser]
☒ À qualifier

`[Demande]` Les **jeux privés envisagés**, potentiellement issus de travaux non publiés de Φ-lab, justifient une vérification explicite de leur confidentialité et des droits d'accès. `[Proposition]` Examiner également le code de plateforme non publié, les soumissions des participants et les logs susceptibles de contenir des identifiants ou informations sensibles ; **leur classification reste à établir**.

**Origine des restrictions :** `[À décider]` Conditions Φ-lab/ESA, droits sur les jeux, licences, conditions du challenge, règles de l'établissement et accords de partenariat à vérifier.
**Informations qui ne doivent pas être soumises à un outil d'IA externe :** `[À décider]` Par précaution, ne transmettre **aucun jeu privé, soumission non autorisée, secret ou configuration sensible** tant que les règles ne sont pas formalisées.
**Une anonymisation ou un jeu de données synthétique suffit-il à lever certaines restrictions ?** ☐ Oui ☐ Non ☒ À valider
**Interlocuteur pour validation SSI / DPO / juridique / valorisation si nécessaire :** [Service / personne à identifier]

### 4.3 Environnement autorisé — décision opérationnelle

☐ **Outils externes approuvés autorisés**, dans les limites précisées ci-dessous (ex. Claude Code, uniquement si autorisé par l'établissement et compatible avec les données).
☐ **Solutions institutionnelles ou souveraines uniquement** (ex. ILaaS, sous réserve de validation du service et de ses garanties effectives).
☐ **Modèles exécutés localement / environnement maîtrisé uniquement**.
☐ **Aucun assistant IA autorisé pour ce projet**.
☒ **Décision différée** : validation requise avant tout usage dans le cadre du projet.

**Outils / modèles / environnements explicitement autorisés :** [À décider]
**Outils explicitement exclus :** [À décider]
**Données et dépôts concernés par l'autorisation :** [À décider]
**Conditions complémentaires :** [À décider : hébergement, rétention, accès réseau, journalisation, etc.]
**Personne habilitée à valider la décision, si nécessaire :** [À identifier]
**Date de validation / révision :** [À fixer]

**Règles communes, quel que soit l'outil :** ne jamais transmettre de secrets d'accès ; relire et tester le code généré ; vérifier licences et dépendances ; conserver une revue humaine des changements ; respecter les règles de sécurité du projet.

## 5. Organisation et calendrier (15 min)

**Rôles et responsabilités :**

| Sujet | Responsable | Contribution attendue |
|---|---|---|
| Arbitrages scientifiques et validation | **Sébastien** `[Demande]` ; participation de Minh-Tan et Pierre [rôles à préciser] | Définition et validation des tâches, métriques, données et critères scientifiques |
| Coordination opérationnelle | Clément | Planning, suivi des tâches, remontée des risques |
| Fourniture des données / code | [Référent équipe scientifique / Φ-lab à désigner] | Accès aux modèles, code, jeux d'évaluation et autorisations associées |
| Infrastructure / support technique | [Référents UBS ou ESA + SSI à désigner] | Environnement GPU, stockage, réseau, isolation et exploitation |
| Développement des workflows de soumission / isolation | [Ingénieur SequoIA responsable à nommer] | Pipeline de soumission, sécurité technique et orchestration |
| Intégration EoS-FM et évaluation | [Ingénieur SequoIA responsable à nommer] | Intégration des modèles, benchmark et reproductibilité |
| Leaderboard / tests / documentation | [Ingénieur SequoIA responsable à nommer] | Interface, pilote, documentation et transfert |

**Charge d'ingénierie envisagée :** **6 personnes-mois** `[Demande]`, formulés comme un ingénieur à temps plein pendant six mois. `[À décider]` Répartition effective entre **deux ingénieurs SequoIA** à 50% sur six mois.
**Période et contraintes de calendrier :** `[Demande]` Démarrage flexible ; challenge visé dans les six mois du début du soutien sous réserve des ressources, données et validations de sécurité. [Date de démarrage et calendrier absolu à confirmer].

| Jalons | Échéance cible | Résultat observable |
|---|---|---|
| M0 — Pré requis levés | `[Proposition]` Début / semaines 1–2 | Accès code, interlocuteurs, décision de démarrage et politique IA clarifiés ; plan des dépendances établi |
| M1 — Premier incrément / MVP | `[Demande]` Travaux principalement aux mois 2–4 ; [date à fixer] | `[Proposition]` Soumission de référence traitée de bout en bout avec évaluation de test et premières garanties d'isolation |
| M2 — Validation | `[Demande]` Mois 4–5 ; [date à fixer] | `[Proposition]` Leaderboard opérationnel, tests d'intégration, contrôle des quotas et de la reproductibilité, validation technique/sécurité selon le contexte |
| M3 — Transfert et clôture | `[Demande]` Mois 6 ; [date à fixer] | Pilote, documentation et passation ; état de préparation au lancement et décisions restantes |

`[Demande]` Calendrier plus détaillé : **mois 1–2** exigences/sécurité/choix des données et infrastructure ; **mois 2–4** soumissions et intégration EoS-FM ; **mois 4–5** leaderboard et tests ; **mois 6** pilote, documentation et préparation du lancement.

**Principaux risques et dépendances :**

| Risque / dépendance | Conséquence | Mesure de réduction | Responsable |
|---|---|---|---|
| Soumissions de code externe non fiable, fuite de jeux privés | Compromission possible de l'infrastructure, du benchmark ou des données | `[Proposition]` Réduire le format accepté ; architecture isolée, contrôles d'accès, quotas et validation SSI **avant code tiers non fiable** | [Hébergeur/SSI + ingénieur responsable à nommer] |
| Jeux privés indisponibles / droits non clarifiés | Retard de validation scientifique et du lancement | `[Proposition]` Clarifier rapidement propriétaire, accès, licences ; données synthétiques/publiques seulement pour les premiers tests | [Équipe scientifique / Φ-lab] |
| Hébergement GPU UBS/ESA indéterminé | Intégration/déploiement retardés | `[Proposition]` Comparer tôt les contraintes des environnements et valider une option exploitable | [Référent infrastructure à nommer] |
| Hétérogénéité et coût GPU des soumissions | Complexité, consommation imprévisible et délais | `[Proposition]` Contrat de soumission limité, quotas, mesure de temps GPU/RAM/stockage, capacité cible | [Ingénieur responsable à nommer] |
| Protocole scientifique non stabilisé | Réécritures, scores non comparables | `[Proposition]` Définir un benchmark pilote et ses métriques avant intégration intensive | [Équipe scientifique] |
| Exploitant post-soutien non identifié | Plateforme difficile à maintenir et à ouvrir au public | `[Proposition]` Désigner l'équipe et les moyens d'exploitation en amont du pilote | [Porteur / hébergeur] |

**Règle en cas d'évolution du périmètre :** `[À décider]` Proposition : arbitrage entre porteur et ingénieurs, mise à jour directe du périmètre et du calendrier dans ce document ; actions de mise en œuvre suivies dans Jira (§7).

## 6. Modalités de collaboration et de suivi (10 min)

**Outil de suivi :** `[Proposition]` Epic « EoS-FM Challenge » dans le Jira commun SequoIA ; [lien à créer].
**Dépôt et documentation technique :** `[Demande]` https://github.com/pierreadorni/EoS-FM pour l'existant. `[À décider]` Dépôt propre à la plateforme ou extension du dépôt scientifique ; droits d'accès, licence et documentation.
**Canal d'échange :** [À décider].
**Cadence de suivi :** ☐ Toutes les 2 semaines ☐ Autre : [Préciser]. **`[Proposition]`** Un point bimensuel de 30 minutes.
**Participants et format des points de suivi :** [Sébastien Lefèvre, autres scientifiques utiles, deux ingénieurs ; à confirmer / démonstrations selon jalons].
**Modalité de validation des livrables :** `[À décider]` Validation scientifique par l'équipe de recherche ; validation de la sécurité et des conditions d'exploitation par les autorités compétentes ; critères de §2 à confirmer.
**Publication / partage / réutilisation :** `[Demande]` Leaderboard public visé. `[À décider]` Licences de la plateforme, conditions de soumission et partage des modèles/résultats, calendrier de publication.

### 6.1 Pérennité et transfert après la fin du soutien

> La demande décrit une plateforme déployable mais **ne désigne pas explicitement ses mainteneurs et exploitants au-delà des six personnes-mois**. Les rôles suivants doivent être confirmés.

| Élément à reprendre | Responsable après soutien | Ressources / modalités de transfert | Statut |
|---|---|---|---|
| Dépôt, versions et corrections | [Équipe scientifique / mainteneur à désigner] | Droits d'administration, documentation, procédure de mise à jour et de correction | ☐ Confirmé ☒ À décider |
| Hébergement et comptes | [Service UBS ou ESA à confirmer] | GPU, stockage, réseau, comptes, budget, sauvegardes | ☐ Confirmé ☒ À décider ☐ Sans objet |
| Données, accès et conformité | [Responsable scientifique / détenteur des jeux à désigner] | Autorisations des jeux privés, protection et durée de conservation, révocation des accès | ☐ Confirmé ☒ À décider ☐ Sans objet |
| Exploitation et assistance utilisateurs | [Organisateurs du challenge / exploitant à désigner] | Gestion des participants, support, incidents, surveillance et runbook | ☐ Confirmé ☒ À décider ☐ Sans objet |

**Modalité de passation et jalon de transfert :** `[Proposition]` Transfert documenté et démonstration d'exploitation lors du mois 6, destinataires et date [à décider].
**Service maintenu au-delà du soutien ?** ☐ Oui, conditions définies ☐ Non, prototype livré ☒ À décider.
**Responsable de la décision de pérennisation :** [Porteur / hébergeur / instance compétente à confirmer].

## 7. Actions à suivre dans Jira (5 min)

> `[Proposition]` Actions candidates à prioriser au kick-off, **non encore attribuées ni engagées**. Ne pas répéter ici les décisions de cadrage : les consigner directement dans les sections 1–6. Après la réunion, créer les tickets correspondant aux actions retenues et ajouter leurs liens ; **Jira devient la référence pour le suivi de leur avancement**.

| Action | Responsable | Contributeur(s) | Échéance | Ticket Jira / lien |
|---|---|---|---|---|
| Auditer le dépôt EoS-FM et reproduire une évaluation de référence | [Ingénieur SequoIA à désigner] | [Second ingénieur, si pertinent] | [À fixer] | [À créer] |
| Formaliser le protocole pilote, les métriques et le contrat de soumission | [Référent scientifique à désigner] | [Ingénieur(s) SequoIA] | [À fixer] | [À créer] |
| Identifier les jeux privés et confirmer droits et modalités d'accès | [Équipe scientifique / Φ-lab à désigner] | [Ingénieur si nécessaire] | [À fixer] | [À créer] |
| Étudier l'hébergement UBS/ESA et les exigences d'isolation/SSI | [Ingénieur SequoIA à désigner] | [Référent infrastructure/SSI à identifier] | [À fixer] | [À créer] |
| Clarifier la politique d'utilisation des assistants IA de développement | [Porteur + autorité compétente à identifier] | [Ingénieurs SequoIA] | [À fixer] | [À créer] |
| Désigner les responsables d'exploitation et de maintenance post-soutien | [Porteur / hébergeur à déterminer] | — | [À fixer] | [À créer] |

**Questions ouvertes / décisions en attente :** format et contraintes des contributions ; protocoles et scores ; jeux privés et droits ; environnement GPU, hébergement, sécurité ; niveau d'ouverture à M6 ; responsables scientifiques/techniques individuels ; répartition des **6 personnes-mois entre deux ingénieurs** ; autorisation des assistants IA ; pérennité. Pour chaque point, préciser **décideur, échéance et impact sur le démarrage ou le pilote** pendant la réunion.
**Prochaine réunion :** [Date / modalité].

## 8. Validation du cadrage

**Le périmètre, les livrables, les responsabilités, les prérequis de démarrage et les modalités de transfert après soutien ont-ils été confirmés ?**
☐ Oui  ☐ Oui, avec réserves listées ci-dessus  ☐ Non — lancement différé

**Référent scientifique :** Sébastien Lefèvre — [date / confirmation]
**Ingénieurs SequoIA :** [Noms, date / confirmation]

> **Après la réunion :** finaliser **ce même document**, actualiser les statuts des informations dans les sections concernées, solliciter une confirmation écrite des responsables (§8), puis créer l’Epic et les tickets Jira correspondant aux actions du §7. Les éléments non validés restent explicitement ouverts, avec responsable et échéance ; ils ne sont pas transformés en engagements implicites. Réviser la section IA si les données, les outils ou les règles changent.
