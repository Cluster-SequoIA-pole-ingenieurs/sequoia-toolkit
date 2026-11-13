# SequoIA — Réunion de lancement d'un soutien d'ingénierie

> **Document unique de cadrage, vivant** · Prérempli avant la réunion, modifié collectivement pendant le kick-off et validé ensuite.
> **Durée indicative :** 60–90 min · **Statut :** `Préparation` · **Dernière mise à jour :** 12/11/2026.
> **Convention :** `☐` à cocher ; compléter les champs `[entre crochets]`. **`[Demande]`** = information issue du dossier ; **`[Décision SequoIA]`** = périmètre accepté communiqué par l'équipe ; **`[Proposition]`** = hypothèse de préparation ; **`[À décider]`** = point à arbitrer ; **`[Validé – date]`** = accord explicite lors du kick-off.
> **Mode d’emploi :** avant la réunion, préremplir les sections 0–6 à partir de la demande EasyChair et des décisions d'acceptation. Pendant le kick-off, **modifier directement les sections concernées** pour refléter le cadrage convenu. Consigner en **section 7 les actions à réaliser**, avec leur responsable, leurs éventuels contributeurs et leur échéance, puis renseigner les tickets dans l'outil de suivi. Après la réunion, finaliser le document et faire valider le cadrage en **section 8**.
> **Périmètre retenu pour ce premier soutien : 6 mois, centré sur T1, T2 et T4.** Les autres volets du projet scientifique pourront faire l'objet d'une **nouvelle demande de soutien** ; ils ne constituent pas un engagement de cette première intervention.

## 0. Identification

| Champ | Valeur |
|---|---|
| Projet / acronyme | **WEIRDEX** — *Global weirding and extremes of extremes: Refining hybrid model–observation analysis of intense storms* |
| Référence de la demande EasyChair | **#46** |
| Date du kick-off | [JJ/MM/AAAA] |
| Porteur / référent scientifique | **Bertrand Chapron**, Ifremer, équipe **ODYSSEY** (LOPS / Lab-STICC / IRMAR) · Bertrand.Chapron@ifremer.fr |
| Ingénieurs SequoIA | **Clément**, **Kamel** — [référent opérationnel à préciser] |
| Autres contributeurs | **Quentin Febvre**, **Alexis Mouche** (Ifremer–LOPS : télédétection et interactions air–mer) ; **Ronan Fablet** (assimilation de données et IA générative) |
| Période de soutien envisagée | **6 mois** — **[Décision SequoIA]** ; date de début et répartition de charge à fixer. La demande initiale évoquait Q1 2027 et ±3 mois de flexibilité pour un programme de 12 mois : calendrier à **revalider pour la tranche de six mois**. |
| Liens de travail | [Dépôt(s) à retenir] · [Espace documentaire] · [Jira ou autre outil de suivi] |

**Participants :** Bertrand, Kamel, Clément [À confirmer]
**Personnes absentes à consulter :** [À compléter]

## 1. Contexte scientifique et résultats recherchés (10 min)

**Problème scientifique / métier — [Demande] :**
Les modèles météorologiques neuronaux reproduisent souvent la trajectoire et les caractéristiques synoptiques des tempêtes mais peuvent sous-estimer leurs intensités extrêmes, notamment les vents de cœur. Les observations satellitaires SAR apportent une description fine des vents de surface, mais leur couverture spatio-temporelle est incomplète. WEIRDEX cherche à articuler observations multi-sources et modèles pour mieux caractériser les tempêtes exceptionnelles (cyclones tropicaux, *medicanes*, tempêtes européennes).

**Objectif du projet à plus long terme — [Demande] :**
Constituer un catalogue multi-source d'événements extrêmes ; comparer systématiquement les modèles météo IA aux observations ; étudier les préconditions atmosphériques et océaniques des événements rares ; puis développer des approches génératives de correction d'intensité et d'incertitude (objectifs scientifiques O1–O4). **Ces quatre objectifs scientifiques ne sont pas tous inclus dans le soutien de six mois.**

**Résultat attendu du soutien SequoIA — [Décision SequoIA + Proposition] :**
Une **chaîne reproductible**, sur un ensemble d'événements et de modèles représentatif à définir, reliant (i) des observations et réanalyses harmonisées en cubes centrés sur les tempêtes (**T1**), (ii) des *hindcasts* de modèles météo neuronaux exécutés sur HPC (**T2**) et (iii) un outil de comparaison quantitative avec les vents SAR et des métriques adaptées aux extrêmes (**T4**). Le niveau de couverture et les critères d'achèvement sont à négocier au kick-off.

**Lien avec les axes de SequoIA — [Proposition, à confirmer] :**
Convergence avec les thématiques **IA pour l'environnement et l'océan**, ainsi qu'avec l'évaluation robuste des modèles IA et l'ingénierie de données scientifiques.

## 2. Périmètre, livrables et critères de réussite (15 min)

### 2.1 Livrables d'ingénierie — première tranche de six mois

| ID | Livrable concret | Critère d'acceptation vérifiable — **[Proposition]** | Validation par |
|---|---|---|---|
| **L1 / T1** | Pipeline de préparation de **cubes multi-sources centrés sur les tempêtes** (ex. xarray/Zarr/Dask), avec métadonnées, traçabilité et contrôles qualité | Exécution documentée et reproductible pour **[N événements]** de **[types de tempêtes]**, à partir de **[sources prioritaires]** ; contrôles de coordonnées, temporalité et qualité disponibles | Bertrand Chapron + référents données **[à confirmer]** |
| **L2 / T2** | Pipeline **conteneurisé de hindcasts** de modèles météo IA sur infrastructure HPC, avec configuration et archivage des sorties | Exécution reproductible de **[N modèles]** sur **[N événements]**, journalisation de la provenance, des paramètres, des échecs et des ressources consommées | Référents scientifiques **[à désigner]** |
| **L3 / T4** | Outil de **comparaison et d'évaluation** modèles ↔ observations SAR, avec résultats de référence | Métriques prioritaires (p. ex. **Vmax**, **Rmax**, profils de vent ; métriques probabilistes si sorties d'ensemble disponibles) calculées sur **[échantillon défini]**, avec cas tests et rapport synthétique | Bertrand Chapron + référents scientifique/validation **[à confirmer]** |
| **L4 / transversal** | Documentation minimale nécessaire à l'exécution, à la reproductibilité et à la passation des **trois livrables précédents** | Instructions d'installation/exécution, configuration, description des données d'entrée/sortie et limites connues utilisables par l'équipe | Référent scientifique **[à confirmer]** |

> **Attention :** L4 correspond à la documentation indispensable pour livrer T1/T2/T4 ; ce n'est **pas** le chantier autonome **T5** (publication ouverte, tutoriels et notebooks), reporté hors de cette première tranche.

**MVP — résultat indispensable à la fin du soutien — [Proposition] :**
Démontrer une chaîne **de bout en bout sur un petit sous-ensemble d'événements et au moins un modèle neuronal**, avec harmonisation des données, exécution d'un hindcast et comparaison chiffrée à une observation SAR de référence. Les valeurs minimales (nombre d'événements, période, modèles, métriques, tolérances) doivent être validées avec l'équipe scientifique.

**Dans le périmètre — [Décision SequoIA] :**
- **T1 — Data engineering :** ingestion, colocalisation, reprojection/rééchantillonnage, cubes événementiels, métadonnées, indicateurs qualité ; **couverture priorisée**.
- **T2 — Neural weather hindcasts :** déploiement de modèles ouverts sélectionnés, conteneurs et exécution HPC, production/traçabilité d'un ensemble défini de *hindcasts*.
- **T4 — Evaluation toolkit :** métriques de tempêtes contre données SAR, comparaison structurée et reproductible ; métriques probabilistes **si pertinentes et réalisables** dans la tranche.
- Tests, reproductibilité et documentation **strictement nécessaires** aux livrables ci-dessus.

**Hors périmètre initial (nouvelle demande éventuelle) :**
- **T3 — Training infrastructure :** infrastructure multi-GPU de (ré)entraînement / *fine-tuning* de modèles génératifs, expériences *gray swan* avec événements exclus, suivi complet des expériences et checkpoints.
- **T5 — Packaging / publication avancée :** publication ouverte complète, tutoriels, notebooks, démonstrateur / explorateur interactif d'événements.
- **O3/O4 au-delà des outils préparatoires :** analyses scientifiques approfondies des préconditions et développement/entraînement de corrections génératives d'intensité.
- Généralisation à **tous** les événements depuis 2014, à **tous** les modèles ou toutes les métriques sans arbitrage sur la charge.

**Hypothèses structurantes — [À décider] :**
Le soutien retenu est de **6 personnes-mois maximum à confirmer dans le cadrage opérationnel**, mobilisés par deux ingénieurs selon une répartition à déterminer. **Les estimations initiales T1 (4 PM) + T2 (3 PM) + T4 (1,5 PM) totalisent 8,5 PM** : une **réduction de périmètre d'environ 2,5 PM d'effort estimé** est donc indispensable si cette estimation reste pertinente. Identifier les sources, événements, modèles et métriques prioritaires avant tout engagement sur une couverture exhaustive. Dépendance aux accès SAR, au stockage, aux GPU, aux licences et aux référents scientifiques.

## 3. État de l'existant et prérequis (10 min)

| Élément | État actuel / emplacement | Responsable de l'accès | Prêt ? |
|---|---|---|---|
| Code, prototypes, modèles | Modèles météo ouverts cités : GraphCast, Pangu-Weather, FourCastNet, AIFS. Code équipe : [CIA-Oceanix/4dvarnet-fm-opencode](https://github.com/CIA-Oceanix/4dvarnet-fm-opencode) ; couverture exacte de T1/T2/T4 à auditer. **[Demande]** | Ronan Fablet / équipe ; [contacts dépôt et modèles à préciser] | ☐ Oui ☐ Non ☒ À vérifier |
| Données et observations | **CyclObs** (SAR, Ifremer–LOPS), ERA5, IBTrACS, Copernicus Marine, SWOT, SMAP/SMOS, produits NOAA/NextGEMS… **[Demande]** ; accès, licence, format, volume et sélection prioritaire à confirmer | Bertrand Chapron, Quentin Febvre, Alexis Mouche / fournisseurs concernés | ☐ Oui ☐ Non ☒ À vérifier |
| Infrastructure et calcul | Pistes citées : **Datarmor** (Ifremer) et éventuellement **Jean Zay** ; disponibilité et droits non confirmés. Besoins annoncés : GPU ≥ **80 Go** et **30–50 To** de stockage rapide pour le périmètre étendu. **[Demande]** | [Contacts UBS/IRISA et Ifremer à nommer] | ☐ Oui ☐ Non ☒ À vérifier |
| Jeux de test / validation | Observations SAR et produits associés ; définir événements témoins, référentiels de vents, règles de colocalisation et méthodes de calcul des métriques | Équipe scientifique — [référent à nommer] | ☐ Oui ☐ Non ☒ À vérifier |
| Documentation et licences | Références scientifiques et liens fournis ; licences des poids des modèles, jeux de données et droits de redistribution à examiner | Équipe scientifique / [référent licences] | ☐ Oui ☐ Non ☒ À vérifier |

### 3.1 Prérequis de démarrage vs dépendances à lever plus tard

> Les jalons de dépendance ci-dessous sont **des hypothèses de préparation**. Aucun élément n'est déclaré « bloquant » sans validation avec les responsables.

| Élément à obtenir / décision | Nécessaire avant… — **[Proposition]** | Statut | Responsable | Date cible / solution transitoire |
|---|---|---|---|---|
| Accès au code de référence, à un échantillon de données et à des cas tests | ☐ Démarrage ☒ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Équipe scientifique | [Date] / données publiques et échantillon limité pour démarrage exploratoire |
| Liste prioritaire de tempêtes, de sources et convention spatio-temporelle des cubes | ☒ Démarrage ☐ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Bertrand Chapron + référents données | [Date] / première liste de 3–5 événements **à discuter** |
| Accès GPU adapté, compatibilité modèles/poids, support Apptainer et quota de calcul | ☐ Démarrage ☒ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | [Ingénieur responsable] + administrateurs HPC | [Date] / test d'un modèle plus léger ou environnement temporaire |
| Stockage, circulation des données Ifremer ↔ cluster, droits et volumes | ☐ Démarrage ☒ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | [Référents données + infrastructure] | [Date] / jeu de données réduit et hébergement proche de la source |
| Protocole de référence SAR et définition des métriques de validation | ☐ Démarrage ☒ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☒ À obtenir ☐ Bloquant | Scientifiques — [référent] | [Date] / métriques minimales et événement témoin |

**Conditions minimales d'engagement de l'ingénieur — [À décider] :** [Accès dépôts et exemple de données, référents disponibles, premier périmètre T1/T2/T4 et environnement de développement ; préciser si un démarrage exploratoire est autorisé.]
**Conditions à satisfaire avant pilote / validation finale — [À décider] :** [Accès aux événements retenus, ressources GPU/stockage suffisantes, protocole d'évaluation, droits d'usage et pipeline reproductible.]
**Décision de démarrage :** ☐ Go ☐ Go limité (activités autorisées : […]) ☐ No-go, en attente de […]. **[À valider]**

## 4. Utilisation d'assistants IA pour le développement (10 min)

> **Objet :** convenir des usages possibles des assistants de programmation (p. ex. Claude Code, assistants locaux) et de leurs limites. La préférence exprimée par le porteur scientifique ne remplace **ni** les règles de sécurité, de confidentialité, de protection des données et de propriété intellectuelle applicables à l'établissement **ni** les conditions contractuelles du projet.

### 4.1 Accord de principe du porteur

**Le porteur souhaite-t-il autoriser les ingénieurs à utiliser des assistants IA pour ce soutien ?**
☐ Oui, sous réserve des restrictions ci-dessous
☐ Non
☒ À confirmer

**Usages envisagés — [Proposition, non autorisés à ce stade] :**
☐ Aide à la rédaction de code  ☐ Refactorisation  ☐ Génération de tests  ☐ Débogage
☐ Documentation  ☐ Revue de code  ☐ Analyse de données / logs  ☐ Autre : [Préciser]

**Usages ou composants explicitement interdits :** [À décider ; ne pas interpréter l'absence d'interdiction comme un accord]

### 4.2 Classification et contraintes des informations

**Le travail comporte-t-il des éléments soumis à des restrictions particulières ?**
☐ Aucun identifié  ☐ Code ou résultats non publiés  ☐ Données personnelles
☐ Données confidentielles de partenaires / industrielles  ☐ Secret contractuel ou propriété intellectuelle sensible
☐ Données ou technologies soumises à des restrictions réglementaires / de sécurité  ☐ Autre : [Préciser]
☒ À qualifier

**Origine des restrictions — [À décider] :** licences des données satellitaires et modèles, conditions d'accès à CyclObs/produits partenaires, règles Ifremer/UBS, éventuels travaux non publiés. **Le caractère confidentiel des données n'est pas établi par la demande : il doit être vérifié.**
**Informations qui ne doivent pas être soumises à un outil d'IA externe :** [Définir les sources, fichiers, logs, poids, clés, éventuels résultats non publics concernés.]
**Une anonymisation ou un jeu de données synthétique suffit-il à lever certaines restrictions ?** ☐ Oui ☐ Non ☒ À valider
**Interlocuteur pour validation SSI / DPO / juridique / valorisation si nécessaire :** [Nom ou service]

### 4.3 Environnement autorisé — décision opérationnelle

☐ **Outils externes approuvés autorisés**, dans les limites précisées ci-dessous (ex. Claude Code).
☐ **Solutions institutionnelles ou souveraines uniquement** (ex. ILaaS, sous réserve de validation).
☐ **Modèles exécutés localement / environnement maîtrisé uniquement**.
☐ **Aucun assistant IA autorisé pour ce projet**.
☒ **Décision différée** : validation requise avant tout usage.

**Outils / modèles / environnements explicitement autorisés :** [À décider]
**Outils explicitement exclus :** [À décider]
**Données et dépôts concernés par l'autorisation :** [À décider]
**Conditions complémentaires :** [À décider : paramétrage, conservation, hébergement, accès réseau, journalisation, etc.]
**Personne habilitée à valider la décision, si nécessaire :** [Nom / service]
**Date de validation / révision :** [Date]

**Règles communes, quel que soit l'outil :** ne jamais transmettre de secrets d'accès ; relire et tester le code généré ; vérifier licences et dépendances ; conserver une revue humaine des changements ; respecter les règles de sécurité du projet.

## 5. Organisation et calendrier (15 min)

**Rôles et responsabilités — [Proposition à discuter] :**

| Sujet / chantier | Responsable | Contribution attendue |
|---|---|---|
| Arbitrages scientifiques, sélection des événements et validation des livrables | Bertrand Chapron (référent) ; [référents thématiques à nommer] | Définir cas prioritaires, métriques et conditions de réussite |
| **T1 — Cubes et pipeline données** | [Clément ou Kamel — à décider] | Mise à disposition des données et expertise SAR / océanographie |
| **T2 — Hindcasts neuronaux / HPC** | [Clément ou Kamel — à décider] | Choix des modèles, accès aux ressources, validation des configurations |
| **T4 — Métriques et benchmark SAR** | [Clément ou Kamel — à décider] | Spécifications scientifiques des métriques et validation des résultats |
| Fourniture du code et des produits SAR | [Référent(s) Ifremer/équipe à nommer] | Comptes, documentation, exemples, droits d'usage |
| Infrastructure / support technique | [Contact Datarmor à identifier] | Ressources GPU/stockage, quotas, conteneurs, transferts |

**Charge d'ingénierie envisagée :** **6 personnes-mois pour cette tranche** — **[Décision SequoIA]**. Répartition entre **Clément et Kamel**, quotités, disponibilité et périmètre priorisé à préciser. **[À décider]**
**Point d'arbitrage essentiel :** les estimations du dossier pour **T1 + T2 + T4 = 8,5 personnes-mois** (4 + 3 + 1,5). Le contenu retenu devra être redimensionné pour tenir dans six personnes-mois, sans présumer que toutes les sorties initiales seront réalisables.
**Période et contraintes de calendrier :** [Date de début – date de fin ; période de six mois]. La préférence Q1 2027 figurant dans la demande initiale **reste à confirmer** pour cette première tranche. Toute poursuite après six mois dépend d'une **nouvelle soumission / acceptation**, sans continuité automatique.

| Jalons | Échéance cible — **[Proposition]** | Résultat observable |
|---|---|---|
| M0 — Prérequis essentiels levés | Mois 1 | Jeux d'essai disponibles, priorités validées, accès de développement, autorisations IA clarifiées |
| M1 — Premier incrément / MVP | Mois 2–3 | Premier cube tempête et premier hindcast sur cas témoin |
| M2 — Validation | Mois 4–5 | Chaîne intégrée et métriques SAR testées sur sélection convenue |
| M3 — Transfert et clôture | Mois 6 | Livrables T1/T2/T4, reproductibilité et documentation minimale validés |

**Principaux risques et dépendances — [Proposition] :**

| Risque / dépendance | Conséquence | Mesure de réduction | Responsable |
|---|---|---|---|
| **8,5 PM estimés pour 6 PM disponibles** | Retard ou livrables incomplets | Limiter événements, sources, modèles, métriques ; définir un MVP et des critères d'acceptation mesurables | Bertrand Chapron + ingénieurs |
| Volume (multi-To), résolutions et échantillonnages hétérogènes | Coûts d'E/S, traitements et stockage importants | Sous-ensemble représentatif, profilage, calcul proche des données, formats chunkés | Responsable T1 + référents données |
| Disponibilité GPU/VRAM et licences des modèles | Hindcasts impossibles ou coûteux | Valider rapidement un cas test, un modèle et une infrastructure ; définir une alternative | Responsable T2 + support HPC |
| Désalignement des champs modèles et mesures SAR | Comparaisons physiquement trompeuses | Définir unités, hauteur du vent, résolutions, fenêtres de collocation et incertitudes | Responsable T4 + référents scientifiques |
| Dépendances d'accès entre Ifremer, UBS et infrastructures nationales | Retards et blocages d'intégration | Confirmer responsabilités, transferts autorisés et quotas dès le début | Référent scientifique + infrastructure |

**Règle en cas d'évolution du périmètre — [À décider] :** [Validation conjointe scientifiques/ingénieurs, révision des livrables et du backlog ; les travaux T3/T5 requièrent une nouvelle demande et ne sont pas ajoutés implicitement.]

## 6. Modalités de collaboration et de suivi (10 min)

**Outil de suivi :** [Jira ou alternative à confirmer ; projet / vue WEIRDEX / lien]
**Dépôt et documentation technique :** [Dépôt(s), branche(s), droits d'accès, emplacement de la documentation]
**Canal d'échange :** [Tchap / courriel / autre, à confirmer]
**Cadence de suivi :** ☐ Toutes les 2 semaines ☐ Autre : [Préciser]
**Participants et format des points de suivi :** [Porteur / référents thématiques, Clément, Kamel ; durée / démonstration]
**Modalité de validation des livrables :** [Référent pour L1/L2/L3, protocole d'acceptation, délai de retour]
**Publication / partage / réutilisation :** **[Demande]** intention de réutilisation et diffusion ouverte ; **[À décider]** licences et possibilité effective de redistribution des données SAR, modèles et sorties, notamment si l'objectif de catalogue ouvert est limité par certaines sources.

### 6.1 Pérennité et transfert après la fin du soutien

> La fin des six mois clôt **cette tranche d'ingénierie**. Une éventuelle seconde phase sera soumise et évaluée séparément. Identifier dès maintenant les personnes chargées de réutiliser, conserver et maintenir les livrables intermédiaires.

| Élément à reprendre | Responsable après soutien | Ressources / modalités de transfert | Statut |
|---|---|---|---|
| Dépôts, versions et corrections T1/T2/T4 | [Équipe ODYSSEY / nom à confirmer] | [Accès mainteneur, versions, tests, documentation] | ☐ Confirmé ☒ À décider |
| Calcul, stockage des cubes et des hindcasts | [Ifremer/UBS/service à confirmer] | [Quotas, coût, archivage, expiration des données] | ☐ Confirmé ☒ À décider ☐ Sans objet |
| Données, accès et conformité | [Référents données Ifremer / nom à confirmer] | [Droits, licences, traçabilité, éventuelles restrictions de partage] | ☐ Confirmé ☒ À décider ☐ Sans objet |
| Exploitation des pipelines et assistance aux futurs utilisateurs | [Équipe scientifique / nom à confirmer] | [Procédures de relance, support, maintenance et continuité] | ☐ Confirmé ☒ À décider ☐ Sans objet |

**Modalité de passation et jalon de transfert :** [Démonstration, dépôt, documentation de reproduction, reprise par l'équipe — mois 6].
**Service maintenu au-delà du soutien ?** ☐ Oui, conditions définies ☐ Non, prototype livré ☒ À décider.
**Responsable de la décision de pérennisation :** [Nom / service à confirmer].

## 7. Actions à suivre dans Jira (5 min)

> **Actions proposées pour préparer la réunion et le démarrage**, à confirmer/attribuer pendant le kick-off. Ne pas dupliquer ici les décisions de cadrage, qui doivent être reportées directement dans les sections concernées. Renseigner ensuite les liens des tickets dans l'outil retenu.

| Action | Responsable | Contributeur(s) | Échéance | Ticket Jira / lien |
|---|---|---|---|---|
| **Arbitrer le MVP de six mois** : événements, produits prioritaires, modèles et métriques afin de ramener 8,5 PM estimés à 6 PM | Bertrand Chapron / [référents scientifiques] | Clément, Kamel | [À fixer, prioritaire] | [À créer] |
| Désigner les responsables de T1, T2 et T4 et définir les disponibilités des deux ingénieurs | [À désigner] | Clément, Kamel | [À fixer] | [À créer] |
| Fournir les accès et exemples de données CyclObs/SAR et autres produits prioritaires, avec leurs conditions d'usage | [Référent Ifremer à désigner] | [Ingénieur T1] | [À fixer] | [À créer] |
| Auditer le dépôt existant et préciser les composants réutilisables pour T1/T2/T4 | [Ingénieur à désigner] | [Équipe scientifique] | [À fixer] | [À créer] |
| Vérifier les ressources GPU/stockage disponibles, Apptainer, quotas et transfert des données entre sites | [Ingénieur T2] | [Support HPC, référent données] | [À fixer] | [À créer] |
| Définir la référence scientifique des métriques SAR et un premier ensemble d'événements de validation | [Référent scientifique à désigner] | [Ingénieur T4] | [À fixer] | [À créer] |
| Qualifier les contraintes de confidentialité/licences et décider des assistants IA autorisés | Bertrand Chapron / [service compétent] | Clément, Kamel | [À fixer] | [À créer] |
| Désigner les responsables de la maintenance, des données et de l'hébergement après la tranche de six mois | Bertrand Chapron / [équipe] | [À confirmer] | [À fixer] | [À créer] |

**Questions ouvertes nécessitant une action :** voir les points `[À décider]` des sections 2 à 6 ; affecter un responsable et une échéance aux tickets correspondants.
**Prochaine réunion :** [Date / modalité]

## 8. Validation du cadrage

**Le périmètre limité à six mois (T1/T2/T4), les livrables, les responsabilités, les prérequis de démarrage et les modalités de transfert après soutien ont-ils été confirmés ?**
☐ Oui  ☐ Oui, avec réserves listées ci-dessus  ☐ Non — lancement différé

**Référent scientifique :** Bertrand Chapron — [Date / confirmation]
**Ingénieurs SequoIA :** Clément, Kamel — [Date / confirmation]

> **Après la réunion :** finaliser **ce même document**, actualiser les statuts des informations dans les sections concernées, solliciter une confirmation écrite (section 8), puis créer les tickets correspondant aux actions de la section 7. L'outil de suivi devient la référence pour l'avancement des actions. **La poursuite éventuelle des travaux T3/T5 ou l'extension de T1/T2/T4 relève d'une nouvelle demande de soutien**, sans engagement automatique dans la présente tranche.
