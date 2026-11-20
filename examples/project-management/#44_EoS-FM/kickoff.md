# SequoIA — Réunion de lancement d'un soutien d'ingénierie — EoS-FM Challenge

> **Document unique de cadrage, vivant** · Prérempli avant la réunion, modifié collectivement pendant le kick-off et validé ensuite.  
> **Durée indicative :** 60–90 min · **Statut :** `Préparation` · **Dernière mise à jour :** 20/11/2026.  
> **Convention :** `☐` à cocher ; compléter les champs `[entre crochets]`. **`[Demande]`** = information présente dans la proposition EasyChair #44 ; **`[Proposition]`** = hypothèse de cadrage non validée ; **`[À décider]`** = question ouverte ; **`[Validé – date]`** = accord explicite.  
> **Mode d’emploi :** avant la réunion, préremplir les sections 0–6 à partir de la demande EasyChair #44, en distinguant informations établies, propositions et points à décider. Pendant le kick-off, **modifier directement les sections concernées** pour refléter le cadrage convenu. Consigner en **section 7 les actions à réaliser**, avec leur responsable, leurs éventuels contributeurs et leur échéance, puis créer ou renseigner les tâches / issues correspondantes dans l'outil de suivi retenu en **section 6**. Après la réunion, finaliser le document et faire valider le cadrage en **section 8**.

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
| Liens de travail | [Dépôt du benchmark / espace documentaire / outil du porteur ou issues et tableau GitHub / GitLab à préciser] ; code scientifique : https://github.com/pierreadorni/EoS-FM ; article : https://arxiv.org/abs/2511.21523 |

**Participants :** Sébastien, Nouhaila, Clément  
**Personnes absentes à consulter :** [À renseigner ; notamment référents hébergement/SSI/ESA selon décisions]

## 1. Contexte scientifique et résultats recherchés (10 min)

**Problème scientifique / métier :**
`[Demande]` Les modèles de fondation en observation de la Terre doivent transférer leurs représentations entre tâches, capteurs et régions. EoS-FM explore une approche modulaire associant des encodeurs spécialistes entraînés sur des jeux de données et tâches différents. Une étude de référence porte sur **22 spécialistes évalués sur 11 tâches PANGAEA**.

**Objectif du projet à plus long terme :**
`[Demande]` Organiser un **challenge international** dans lequel des équipes soumettent des collections de modèles spécialistes. Un protocole commun et des **jeux de test privés** permettront de comparer les contributions, de mieux comprendre leur complémentarité et de favoriser l'émergence d'un modèle géospatial de référence.

**Résultat attendu du soutien SequoIA :**
`[Proposition]` Un **benchmark EoS-FM déployable sur Codabench**, permettant de déposer des collections de spécialistes, de les évaluer avec un pipeline contrôlé par les organisateurs et de publier des résultats comparables pour une version donnée. Le protocole, les contraintes de soumission et les métriques restent à établir avec l'équipe scientifique et les partenaires éventuels.

**Lien avec les axes de SequoIA :** Contribution aux travaux sur les fondations de l'IA (ensembles de modèles spécialistes, évaluation robuste) et aux applications en observation de la Terre / environnement. La demande mentionne un soutien du cluster via la **chaire PANORAMIX**, ainsi que CNES, UBS et ANR DREAMS autour du projet scientifique.

## 2. Périmètre, livrables et critères de réussite (15 min)

### 2.1 Livrables d'ingénierie

| ID | Livrable concret | Critère d'acceptation vérifiable | Validation par |
|---|---|---|---|
| L1 | **Benchmark Codabench déployable et versionné** : soumissions de collections, suivi des évaluations et leaderboard | Une soumission de référence suit le parcours dépôt → validation → évaluation → publication sur l'instance cible ; une phase continue sans date de fin est configurée ; permissions vérifiées avec des comptes organisateur et participant | [Porteur + responsable plateforme à confirmer] |
| L2 | **Pipeline scientifique EoS-FM intégré et reproductible**, sur un ensemble initial de tâches réelles | Une référence scientifique convenue est reproduite avec une tolérance et des seeds explicites ; adaptation des bandes, assemblage, entraînement aval et métriques documentés ; chaque résultat est relié aux versions du modèle, du protocole, des données et de l'environnement | [Équipe scientifique, référent à désigner] |
| L3 | **Contrat de soumission et environnement d'exécution maîtrisés** | Une collection conforme est acceptée ; formats invalides et dépassements de ressources sont traités ; le code participant ne peut accéder aux labels privés de test ni modifier le protocole d'entraînement aval ; accès réseau, fichiers, journaux et sorties vérifiés sur l'environnement cible | [Responsable technique + hébergeur/SSI à désigner] |
| L4 | **Politique de protection du test et de comparabilité à long terme**, accompagnée de son mécanisme d'application initial | Budget d'évaluations et retour participant définis ; quotas et exceptions vérifiés ; aucun détail interdit du test n'est accessible via interface, API, logs ou fichiers ; une procédure de changement de version préserve les résultats antérieurs sans mélanger les scores | [Équipe scientifique + futur exploitant à désigner] |
| L5 | **Kit participant, pilote et dossier d'exploitation/transfert** | Un participant réalise une soumission à partir du kit et d'exemples publics disjoints du test ; l'exploitant désigné réalise un déploiement, traite un échec/reprise et retrouve la traçabilité d'un résultat ; limites, coûts mesurés et conditions d'ouverture sont consignés | [Porteur + futur exploitant + hébergeur, à confirmer] |

**MVP — résultat indispensable à la fin du soutien :**
`[Proposition]` Une version initiale du benchmark sur un **petit ensemble de tâches réelles convenues**, intégrant une référence EoS-FM, un **format de soumission contraint**, une exécution validée pour ce format, un score publié selon une politique de retour limitée, des quotas applicables et un transfert documenté.   **Niveau d'ouverture à six mois** (pilote fermé, accès sur invitation ou ouverture publique) `[À décider]`.

**Dans le périmètre :**
- `[Proposition]` Réutiliser Codabench pour les comptes, dépôts, files d'exécution, statuts et affichage des résultats ; développer l'intégration scientifique et les contrôles spécifiques au benchmark.
- `[Proposition]` Spécifier une collection d'encodeurs : architecture, poids, bandes/modalités, format des représentations, versions, licences et provenance d'entraînement ; fournir le kit et les contrôles de conformité associés.
- `[Proposition]` Fixer les prétraitements, l'adaptation des capteurs/bandes, la fusion des spécialistes et les têtes aval côté organisateur ; entraîner les têtes selon un budget commun et évaluer sur des labels privés séparés.
- `[Proposition]` Déployer une file dédiée et des workers adaptés aux GPU et volumes de données ; contrôler les ressources, les sorties publiées et la traçabilité ; documenter maintenance, changement de version et reprise d'incident.

**Hors périmètre initial (évolutions possibles) :**
- `[Proposition]` Accepter sans restriction du code, des conteneurs, frameworks ou installations de dépendances fournis par les participants.
- `[Proposition]` Refaire un portail de soumission ou un ordonnanceur déjà assuré par Codabench ; couvrir immédiatement toutes les tâches PANGAEA et tous les capteurs.
- `[Proposition]` Fusionner automatiquement les contributions de plusieurs équipes en un modèle communautaire ; cette exploitation scientifique et ses droits de réutilisation sont distincts de l'évaluation individuelle des collections.
- `[Proposition]` Garantir l'absence de surapprentissage sur un test consulté indéfiniment.

### 2.2 Choix structurants à confirmer

| Sujet | Orientation proposée | Arbitrage / validation attendue |
|---|---|---|
| Service et plateforme | Benchmark continu sur Codabench, sans phase de développement ; exemples publics pour les vérifications locales | `[À décider]` Instance utilisée, versions serveur/worker, conditions d'accès et niveau d'ouverture |
| Format accepté | Architectures autorisées et poids dans un format contrôlé pour limiter le risque ; code personnalisé seulement si son exécution peut être isolée du pipeline de confiance | `[À décider]` Architectures, formats, dépendances, taille/nombre de spécialistes, contrats spatiaux/temporels et bandes ; validation SSI selon le format retenu |
| Protocole scientifique | Encodeurs gelés et têtes aval entraînées par les organisateurs avec budget commun comme première configuration | `[À décider]` Tâches, adaptation des bandes, fusion/sélection, normalisation, graines, budget d'entraînement et éventuel fine-tuning ; règles sur les modalités manquantes |
| Résultat publié | Agrégat à précision limitée ; diagnostics détaillés réservés aux organisateurs ; pas de prédictions ou de logs privés publiés | `[À décider]` Métriques par tâche, sens/normalisation, pondération, précision, gestion des tâches manquantes et des ex æquo |
| Prévention de l'adaptation au test | Limiter les requêtes par équipe et le retour des scores ; validation locale sur exemples publics | `[À décider]` Quotas quotidiens et budget glissant, exceptions/réexécutions comptées |
| Comparabilité et pérennité | Versions immuables des données/protocoles et résultats séparés lors d'un changement scientifique | `[À décider]` Politique de renouvellement, archivage et réévaluation des modèles ; gouvernance scientifique et budget d'exploitation |

**Hypothèses structurantes :** `[À décider]` Disponibilité et droits sur un premier ensemble de tâches réelles ; référence reproductible fournie par l'équipe scientifique ; hébergement autorisant le format de soumission retenu ; capacité GPU et stockage ; disponibilités des validateurs ; contribution éventuelle d'ESA Φ-lab et moyens de fonctionnement après soutien.

## 3. État de l'existant et prérequis (10 min)

| Élément | État actuel / emplacement | Responsable de l'accès | Prêt ? |
|---|---|---|---|
| Code, prototypes, modèles | `[Demande]` Dépôt EoS-FM et spécialistes préentraînés : https://github.com/pierreadorni/EoS-FM ; version de référence et conditions de reproduction à convenir | Équipe scientifique IRISA [contact à préciser] | ☐ Oui ☐ Non ☒ À vérifier |
| Données et annotations | `[Demande]` Jeux publics des travaux EoS-FM ; jeux non publiés évoqués par Φ-lab, sans disponibilité ou droits confirmés | Équipe scientifique / interlocuteur Φ-lab [à désigner] | ☐ Oui ☐ Non ☒ À vérifier |
| Infrastructure et calcul | `[Demande]` Accès passé à IDRIS Jean Zay pour la recherche ; UBS ou ESA envisagés pour l'exploitation. `[Proposition]` Instance Codabench reliée à une file dédiée et à des workers GPU | [Référents instance, hébergement et SSI à désigner] | ☐ Oui ☐ Non ☒ À vérifier |
| Jeux de test / validation | `[Demande]` Référence scientifique PANGAEA. `[À décider]` Première suite privée, séparation géographique/temporelle, contrôle des recouvrements avec le préentraînement | Équipe scientifique / détenteurs des jeux | ☐ Oui ☐ Non ☒ À vérifier |
| Documentation et licences | `[Demande]` Article : https://arxiv.org/abs/2511.21523 ; code disponible. `[À décider]` Droits sur code, poids, jeux privés, conservation et réévaluation des contributions | Équipe scientifique / services compétents | ☐ Oui ☐ Non ☒ À vérifier |

### 3.1 Prérequis de démarrage vs dépendances à lever plus tard

> Distinguer ce qui empêche le démarrage, ce qui conditionne seulement l'intégration, le pilote ou l'ouverture. Le tableau propose des phases de besoin ; le caractère bloquant et les responsables restent à arbitrer pendant le kick-off.

| Élément à obtenir / décision | Nécessaire avant… | Statut | Responsable | Date cible / solution transitoire |
|---|---|---|---|---|
| Accès au dépôt scientifique et interlocuteur pour la référence | ☒ Démarrage ☐ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Équipe scientifique + ingénieurs | [Date] ; lecture du dépôt public pour le cadrage |
| Référence reproductible, tâches initiales et contrat scientifique/de soumission | ☐ Démarrage ☒ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Référent scientifique + ingénieurs | [Date] ; tests de format sur données publiques/synthétiques |
| Accès à l'instance Codabench et environnement GPU d'intégration | ☐ Démarrage ☒ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Administrateur instance + hébergeur | [Date] ; essais locaux de confiance en attendant |
| Jeux réels, labels privés, droits d'usage et séparation des accès | ☐ Démarrage ☐ Intégration ☒ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Équipe scientifique / détenteurs des jeux | [Date] ; jeux publics pour l'intégration, sans remplacer le pilote scientifique convenu |
| Format accepté, isolation, ressources et absence de fuite vérifiés sur l'hôte cible | ☐ Démarrage ☐ Intégration ☒ Pilote ☒ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Hébergeur/SSI + responsable technique | [Date] ; uniquement code de confiance avant validation de l'exécution de soumissions tierces |
| Quotas et retour participant | ☐ Démarrage ☐ Intégration ☒ Pilote ☒ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Référent scientifique + futur exploitant | [Date] ; validation manuelle possible des demandes avant évaluation |
| Exploitant, gouvernance scientifique et moyens après soutien | ☐ Démarrage ☐ Intégration ☐ Pilote ☒ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Porteur + hébergeur | [Date] ; transfert limité et durée de service à convenir |

**Conditions minimales d'engagement de l'ingénieur :** `[À décider]` Accès au code, interlocuteurs scientifiques disponibles et activités autorisées clarifiées ; un démarrage limité au cadrage et aux essais de confiance peut précéder le choix définitif de l'hôte ou l'accès aux jeux privés.  
**Conditions à satisfaire avant pilote / ouverture externe :** `[Proposition]` Protocole réel validé, droits d'usage acquis, isolation et accès vérifiés sur l'instance cible, quotas et publication testés avec un compte participant, responsables de validation et d'exploitation identifiés.  
**Décision de démarrage :** ☐ Go ☐ Go limité (activités autorisées : [à définir]) ☐ No-go, en attente de [à définir]. **`[À décider]`**

## 4. Utilisation d'assistants IA pour le développement (10 min)

> **La demande EasyChair ne mentionne aucune autorisation d'utiliser des assistants IA.** Les questions suivantes concernent les outils de développement des ingénieurs, distincts des modèles participants au challenge.

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
| Arbitrages scientifiques et validation | Sébastien `[Demande]` ; Minh-Tan et Pierre [rôles à préciser] | Référence, tâches, métriques, protocole, conditions de publication |
| Coordination opérationnelle | Clément | Planning, suivi des tâches et des dépendances, remontée des risques |
| Fourniture des données / code | [Référent équipe scientifique / Φ-lab à désigner] | Versions de référence, jeux d'évaluation, provenance et autorisations |
| Instance Codabench, infrastructure et sécurité | [Administrateur instance + hébergeur UBS/ESA + SSI à désigner] | File/workers GPU, stockage, accès, limites de ressources, exploitation |
| Contrat de soumission et intégration scientifique | [Ingénieur SequoIA responsable à nommer] | Interface des spécialistes, adaptation EoS-FM, reproductibilité et tests scientifiques |
| Déploiement, protection du test et transfert | [Ingénieur SequoIA responsable à nommer] | Configuration, quotas, contrôles de publication, validation technique et procédures d'exploitation |

**Charge d'ingénierie envisagée :** **6 personnes-mois** `[Demande]`, formulés comme un ingénieur à temps plein pendant six mois. `[À décider]` Répartition effective entre deux ingénieurs SequoIA ; hypothèse de 50 % chacun pendant six mois à confirmer.

**Période et contraintes de calendrier :** `[Demande]` Lancement visé dans les six mois suivant le début du soutien, sous réserve des ressources, données et validations. `[Proposition]` Distinguer la livraison initiale du benchmark et son fonctionnement récurrent sur les mois/années suivants ; dates absolues et niveau d'ouverture à confirmer.

| Jalons | Échéance cible | Résultat observable |
|---|---|---|
| M0 — Prérequis de démarrage clarifiés | `[Proposition]` Début / semaines 1–2 | Accès, interlocuteurs et activités autorisées ; décisions de démarrage et IA ; plan des dépendances |
| M1 — Premier incrément / MVP | `[Proposition]` Mois 2–4, après cadrage aux mois 1–2 | Collection de référence évaluée sur une première tâche réelle via l'adaptateur EoS-FM ; contrat et budget d'évaluation convenus ; parcours Codabench démontré |
| M2 — Validation scientifique et technique | `[Proposition]` Mois 4–5 | Suite initiale et référence validées ; quotas, accès, sorties, erreurs/reprises et coûts vérifiés sur l'hôte cible ; procédure de versionnement testée |
| M3 — Pilote, transfert et décision d'ouverture | `[Demande]` Mois 6 ; [date à fixer] | Pilote représentatif, guides participant/exploitant, responsables et moyens de reprise ; conditions d'ouverture et plan de renouvellement actés ou réserves explicites |

**Principaux risques et dépendances :**

| Risque / dépendance | Conséquence | Mesure de réduction | Responsable |
|---|---|---|---|
| Code tiers ou fichiers de poids non fiables ; accès aux labels privés ou modification de l'entraînement aval | Compromission de l'hôte, fuite de données ou scores scientifiquement invalides | `[Proposition]` Format/architectures autorisés, contrôle des fichiers, séparation du code tiers et du pipeline de confiance, validation sur l'hôte avant soumissions externes | [Responsable technique + hébergeur/SSI] |
| Adaptation répétée au test à partir des scores | Performance surestimée et perte de valeur du benchmark | `[Proposition]` Budget par équipe, retour limité, contrôles des recouvrements, données renouvelables ; aucune promesse d'absence totale de surapprentissage | [Référent scientifique + exploitant] |
| Jeux réels ou droits non disponibles | Validation scientifique et ouverture retardées | `[Proposition]` Identifier tôt les jeux/propriétaires et un premier périmètre réaliste ; données publiques/synthétiques réservées aux essais appropriés | [Équipe scientifique / Φ-lab] |
| Hôte GPU ou capacité insuffisante, coût des collections hétérogènes | Files d'attente, dépassement du budget ou indisponibilité | `[Proposition]` Mesurer le coût d'une évaluation représentative, plafonner ressources et format, dimensionner les workers ; limiter le nombre initial de tâches | [Hébergeur + ingénieur responsable] |
| Changement de données, métriques ou environnement sans version distincte | Scores historiques non comparables | `[Proposition]` Références et configurations figées, provenance complète, nouvelles versions publiées séparément, réévaluations explicites | [Équipe scientifique + mainteneur] |
| Exploitation et renouvellement du benchmark non financés après le soutien | Service interrompu ou test surexposé | `[Proposition]` Attribuer maintenance, support, budget GPU/stockage et revues scientifiques avant l'ouverture durable | [Porteur + hébergeur] |

**Règle en cas d'évolution du périmètre :** `[Proposition]` Arbitrage porteur/ingénieurs ; mise à jour du cadrage et du calendrier dans ce document ; actions d'application suivies dans l'outil retenu en section 6. Tout changement affectant la comparabilité d'une évaluation implique un arbitrage scientifique sur la version du benchmark.

## 6. Modalités de collaboration et de suivi (10 min)

> **Choix de l'outil :** utiliser l'outil de suivi du porteur s'il en dispose déjà. Sinon, utiliser les issues du dépôt GitHub / GitLab du projet et un tableau associé (GitHub Projects ou tableau d'issues GitLab, par exemple en Kanban).

**Solution retenue :** ☐ Outil existant du porteur ☐ Issues et tableau GitHub / GitLab. **`[À décider]`**  
**Outil de suivi et tableau du projet :** [Nom / URL de l'outil du porteur ou liens vers les issues et le tableau].  
**Responsable de la mise en place et des accès :** [À désigner ; accès au porteur et aux deux ingénieurs].  
**Organisation du suivi des tâches :** `[Proposition]` Responsable, priorité, échéance et éventuel blocage par tâche ; statuts À faire / En cours / À valider / Terminé ; jalons reliés aux livrables L1–L5.  
**Journal de suivi :** [Lien vers le journal cumulatif du soutien] — modèle : [journal de suivi](../../../templates/project-management/follow-up.md).  

> **Éviter la double saisie :** ce kick-off reste la référence du cadrage ; l'outil retenu porte le détail des tâches, responsables, statuts et échéances ; le journal rassemble avancées significatives, blocages, décisions et priorités, avec liens vers les tâches.

**Dépôt et documentation technique :** `[Demande]` https://github.com/pierreadorni/EoS-FM pour le code scientifique. `[À décider]` Dépôt du benchmark distinct ou extension du dépôt scientifique ; droits, licence et responsabilités de mise à jour. `[Proposition]` Versionner configuration, adaptateurs, kit et procédures ; conserver données privées et secrets hors des dépôts publics.  
**Canal d'échange :** [À décider].  
**Cadence de suivi :** ☐ Toutes les 2 semaines ☐ Autre : [Préciser]. `[Proposition]` Point de 30 minutes toutes les deux semaines.  
**Participants et format des points de suivi :** [Sébastien, scientifiques utiles et deux ingénieurs ; à confirmer / démonstrations selon jalons].  
**Modalité de validation des livrables :** `[Proposition]` Validation scientifique par le référent désigné, validation technique et sécurité par les responsables compétents, puis acceptation par le porteur sur les critères du §2 ; délai de retour [à fixer].  
**Publication / partage / réutilisation :** `[Demande]` Leaderboard public visé. `[À décider]` Licences, droits de conservation et réévaluation des modèles, visibilité des métadonnées, retour de scores, archives de versions et annonces de changement de protocole.

### 6.1 Pérennité et transfert après la fin du soutien

| Élément à reprendre | Responsable après soutien | Ressources / modalités de transfert | Statut |
|---|---|---|---|
| Dépôt, versions et corrections | [Mainteneur scientifique/technique à désigner] | Droits, versions serveur/worker et image d'évaluation, procédure de correction et de publication sans mélange des résultats | ☐ Confirmé ☒ À décider |
| Hébergement et comptes | [Administrateur instance + service UBS/ESA à confirmer] | GPU, stockage, réseau, sauvegardes et budget récurrent ; distinguer exploitation de l'instance et celle des workers | ☐ Confirmé ☒ À décider ☐ Sans objet |
| Données, accès et conformité | [Détenteur des jeux + référent scientifique à désigner] | Droits, séparation des labels privés, conservation des soumissions et résultats, révocation et renouvellement des accès | ☐ Confirmé ☒ À décider ☐ Sans objet |
| Exploitation et assistance utilisateurs | [Exploitant à désigner] | Admission, budgets d'évaluation et exceptions, incidents, files GPU, contrôle des sorties et procédures de reprise | ☐ Confirmé ☒ À décider ☐ Sans objet |
| Gouvernance scientifique | [Équipe / référent à désigner] | Revues espacées, réserve de données indépendante, renouvellement/versionnement et réévaluation des modèles archivés | ☐ Confirmé ☒ À décider |

**Modalité de passation et jalon de transfert :** `[Proposition]` Démonstration d'exploitation au mois 6, remise des accès/procédures et exercice de reprise par le destinataire ; périmètre de maintenance et limites convenus par écrit.  
**Service maintenu au-delà du soutien ?** ☐ Oui, conditions définies ☐ Non, prototype livré ☒ À décider.  
**Responsable de la décision de pérennisation :** [Porteur / hébergeur / instance compétente à confirmer].

## 7. Actions à suivre dans l'outil retenu (5 min)

> Actions candidates à prioriser au kick-off, non encore attribuées ni engagées. Les décisions de cadrage se renseignent directement dans les sections 1–6. Après la réunion, créer ou renseigner les tâches / issues retenues dans l'outil du §6 et compléter les liens ; cet outil devient la référence pour leur avancement, sans double mise à jour de ce tableau.

| Action | Responsable | Contributeur(s) | Échéance | Tâche / issue / lien |
|---|---|---|---|---|
| Choisir l'outil de suivi, donner les accès et ouvrir le journal cumulatif | [Clément / référent porteur à confirmer] | [Ingénieurs] | [À fixer] | [À créer] |
| Fixer la référence EoS-FM, les tâches initiales, le contrat de soumission et les critères scientifiques | [Référent scientifique à désigner] | [Ingénieurs, Pierre / Minh-Tan selon rôles] | [À fixer] | [À créer] |
| Confirmer jeux, droits et séparation du test| [Équipe scientifique / détenteurs des jeux] | [Φ-lab si contribution confirmée] | [À fixer] | [À créer] |
| Désigner instance/hébergeur et valider format, isolation, GPU, stockage et capacité cible | [Responsable technique à désigner] | [Administrateur instance, hébergeur/SSI] | [À fixer] | [À créer] |
| Arrêter la politique de budgets, retour des scores, exceptions et versions | [Référent scientifique + futur exploitant] | [Ingénieurs] | [À fixer] | [À créer] |
| Clarifier la politique d'utilisation des assistants IA de développement | [Porteur + autorité compétente] | [Ingénieurs] | [À fixer] | [À créer] |
| Confirmer le niveau d'ouverture à M6 et les responsables/moyens de fonctionnement après soutien | [Porteur + hébergeur] | [Référent scientifique, futur exploitant] | [À fixer] | [À créer] |

**Questions ouvertes nécessitant une action :** reporter dans le tableau les points restants des §2.2, §3.1 et §6.1, avec décideur, échéance et impact sur le démarrage, le pilote ou l'ouverture ; confirmer également la répartition des six personnes-mois entre les deux ingénieurs.  
**Prochaine réunion :** [Date / modalité].

## 8. Validation du cadrage

**Le périmètre, les livrables, les responsabilités, les prérequis de démarrage et les modalités de transfert après soutien ont-ils été confirmés ?**
☐ Oui  ☐ Oui, avec réserves listées ci-dessus  ☐ Non — lancement différé

**Référent scientifique :** Sébastien Lefèvre — [date / confirmation]  
**Ingénieurs SequoIA :** [Noms, date / confirmation]

> **Après la réunion :** finaliser **ce même document**, actualiser les statuts des informations dans les sections concernées, solliciter une confirmation écrite des responsables (§8), puis mettre en place les accès et le tableau de suivi si nécessaire, créer ou renseigner les tâches / issues correspondant aux actions du §7 dans l'outil retenu au §6 et compléter leurs liens. Les éléments non validés restent explicitement ouverts, avec responsable et échéance ; ils ne sont pas transformés en engagements implicites. Réviser la section IA si les données, les outils ou les règles changent.
