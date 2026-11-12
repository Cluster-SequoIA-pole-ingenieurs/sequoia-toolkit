# SequoIA — Réunion de lancement d'un soutien d'ingénierie

> **Document unique de cadrage, vivant** · Prérempli avant la réunion, modifié collectivement pendant le kick-off et validé ensuite.
> **Durée indicative :** 60–90 min · **Statut :** `[Préparation / En discussion / Validé / À réviser]` · **Dernière mise à jour :** `[date]`.  
> **Convention :** `☐` à cocher ; compléter les champs `[entre crochets]`. Pour les informations sensibles ou structurantes, conserver le statut de l'information : **`[Demande]`** (proposition déposée), **`[Proposition]`** (hypothèse de travail), **`[À décider]`** (point ouvert), **`[Validé – date]`** (accord explicite).  
> **Pendant la réunion :** modifier les sections 1–6 *en place* pour refléter le cadrage discuté ; consigner **uniquement les changements significatifs, décisions, réserves et actions** en section 7. Après la réunion, la version validée des sections 1–6 fait foi ; la section 7 en garde la trace.

## 0. Identification

| Champ | Valeur |
|---|---|
| Projet / acronyme | [Nom] |
| Référence de la demande EasyChair | [ID / lien] |
| Date du kick-off | [JJ/MM/AAAA] |
| Porteur / référent scientifique | [Nom, laboratoire, contact] |
| Ingénieurs SequoIA | [Nom 1] (référent), [Nom 2] |
| Autres contributeurs | [Noms et rôles] |
| Période de soutien envisagée | [Début – fin] |
| Liens de travail | [Dépôt Git, espace documentaire, Jira, etc.] |

**Participants :** [Noms]  
**Personnes absentes à consulter :** [Noms / aucune]

## 1. Contexte scientifique et résultats recherchés (10 min)

**Problème scientifique / métier :**  
[En quelques phrases, quel problème motive la demande ?]

**Objectif du projet à plus long terme :**  
[Objectif scientifique, distinct du soutien d'ingénierie.]

**Résultat attendu du soutien SequoIA :**  
[Quelle capacité nouvelle, démonstration, expérimentation ou infrastructure sera disponible à la fin ?]

**Lien avec les axes de SequoIA :**  
[Axes / piliers pertinents et justification synthétique.]

## 2. Périmètre, livrables et critères de réussite (15 min)

### 2.1 Livrables d'ingénierie

| ID | Livrable concret | Critère d'acceptation vérifiable | Validation par |
|---|---|---|---|
| L1 | [Ex. pipeline reproductible] | [Ex. exécution documentée sur un jeu de test] | [Nom / rôle] |
| L2 | [Ex. prototype logiciel] | [Ex. fonctions essentielles testées] | [Nom / rôle] |
| L3 | [Ex. documentation / transfert] | [Ex. procédure d'installation et de prise en main] | [Nom / rôle] |

**MVP — résultat indispensable à la fin du soutien :**  
[Décrire une version minimale démontrable, même si le projet complet est plus ambitieux.]

**Dans le périmètre :**  
- [Tâche / composant]
- [Tâche / composant]

**Hors périmètre initial (évolutions possibles) :**  
- [Fonctionnalité / expérimentation]
- [Fonctionnalité / expérimentation]

**Hypothèses structurantes :** [Données disponibles, accès aux infrastructures, contributions du laboratoire, etc.]

## 3. État de l'existant et prérequis (10 min)

| Élément | État actuel / emplacement | Responsable de l'accès | Prêt ? |
|---|---|---|---|
| Code, prototypes, modèles | [URL, version, maturité] | [Nom] | ☐ Oui ☐ Non ☐ À vérifier |
| Données et annotations | [Description, format, volume] | [Nom] | ☐ Oui ☐ Non ☐ À vérifier |
| Infrastructure et calcul | [Machines, GPU, stockage, comptes] | [Nom] | ☐ Oui ☐ Non ☐ À vérifier |
| Jeux de test / validation | [Protocole ou référence] | [Nom] | ☐ Oui ☐ Non ☐ À vérifier |
| Documentation et licences | [Liens et conditions de réutilisation] | [Nom] | ☐ Oui ☐ Non ☐ À vérifier |

### 3.1 Prérequis de démarrage vs dépendances à lever plus tard

> Distinguer ce qui **empêche de commencer le travail d'ingénierie**, ce qui **bloquerait seulement une phase ultérieure** (pilote, déploiement, ouverture), et ce qui peut rester ouvert sans bloquer. Le statut doit être décidé avec les responsables, pas déduit de la seule existence d'un risque.

| Élément à obtenir / décision | Nécessaire avant… | Statut | Responsable | Date cible / solution transitoire |
|---|---|---|---|---|
| [Ex. accès au dépôt de code] | ☐ Démarrage ☐ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☐ À obtenir ☐ Bloquant | [Nom] | [Date / alternative] |
| [Ex. jeux privés et droits d'usage] | ☐ Démarrage ☐ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☐ À obtenir ☐ Bloquant | [Nom] | [Date / données synthétiques] |
| [Ex. infrastructure et feu vert SSI] | ☐ Démarrage ☐ Intégration ☐ Pilote ☐ Mise en production | ☐ Acquis ☐ À obtenir ☐ Bloquant | [Nom] | [Date / environnement de développement] |

**Conditions minimales d'engagement de l'ingénieur :** [Liste convenue ; éventuellement « aucune, démarrage exploratoire autorisé »].  
**Conditions à satisfaire avant pilote / ouverture externe :** [Liste convenue].  
**Décision de démarrage :** ☐ Go ☐ Go limité (activités autorisées : […]) ☐ No-go, en attente de […]. **[À valider]**

## 4. Utilisation d'assistants IA pour le développement (10 min)

> **Objet :** convenir des usages possibles des assistants de programmation (p. ex. Claude Code, assistants locaux) et de leurs limites. La préférence exprimée par le porteur scientifique ne remplace **ni** les règles de sécurité, de confidentialité, de protection des données et de propriété intellectuelle applicables à l'établissement **ni** les conditions contractuelles du projet.

### 4.1 Accord de principe du porteur

**Le porteur souhaite-t-il autoriser les ingénieurs à utiliser des assistants IA pour ce soutien ?**  
☐ Oui, sous réserve des restrictions ci-dessous  
☐ Non  
☐ À confirmer

**Usages envisagés :**  
☐ Aide à la rédaction de code  ☐ Refactorisation  ☐ Génération de tests  ☐ Débogage  
☐ Documentation  ☐ Revue de code  ☐ Analyse de données / logs  ☐ Autre : [Préciser]

**Usages ou composants explicitement interdits :** [Préciser / aucun identifié]

### 4.2 Classification et contraintes des informations

**Le travail comporte-t-il des éléments soumis à des restrictions particulières ?**  
☐ Aucun identifié  ☐ Code ou résultats non publiés  ☐ Données personnelles  
☐ Données confidentielles de partenaires / industrielles  ☐ Secret contractuel ou propriété intellectuelle sensible  
☐ Données ou technologies soumises à des restrictions réglementaires / de sécurité  ☐ Autre : [Préciser]  
☐ À qualifier

**Origine des restrictions :** [Contrat, convention de partenariat, financeur, politique SSI, licence, RGPD, etc.]  
**Informations qui ne doivent pas être soumises à un outil d'IA externe :** [Fichiers, dépôts, extraits de code, prompts, logs, secrets, jeux de données, etc.]  
**Une anonymisation ou un jeu de données synthétique suffit-il à lever certaines restrictions ?** ☐ Oui ☐ Non ☐ À valider  
**Interlocuteur pour validation SSI / DPO / juridique / valorisation si nécessaire :** [Nom ou service]

### 4.3 Environnement autorisé — décision opérationnelle

☐ **Outils externes approuvés autorisés**, dans les limites précisées ci-dessous (ex. Claude Code, uniquement si autorisé par l'établissement et compatible avec les données).  
☐ **Solutions institutionnelles ou souveraines uniquement** (ex. ILaaS, sous réserve de validation du service et de ses garanties effectives).  
☐ **Modèles exécutés localement / environnement maîtrisé uniquement**.  
☐ **Aucun assistant IA autorisé pour ce projet**.  
☐ **Décision différée** : validation requise avant tout usage.

**Outils / modèles / environnements explicitement autorisés :** [Noms, versions ou catégories, conditions]  
**Outils explicitement exclus :** [Noms / catégories]  
**Données et dépôts concernés par l'autorisation :** [Périmètre exact]  
**Conditions complémentaires :** [Paramétrage, conservation, hébergement, accès réseau, journalisation, etc.]  
**Personne habilitée à valider la décision, si nécessaire :** [Nom / service]  
**Date de validation / révision :** [Date]

**Règles communes, quel que soit l'outil :** ne jamais transmettre de secrets d'accès ; relire et tester le code généré ; vérifier licences et dépendances ; conserver une revue humaine des changements ; respecter les règles de sécurité du projet.

## 5. Organisation et calendrier (15 min)

**Rôles et responsabilités :**

| Sujet | Responsable | Contribution attendue |
|---|---|---|
| Arbitrages scientifiques et validation | [Référent scientifique] | [Décisions / retours] |
| Coordination opérationnelle | [Ingénieur 1] | [Planning, tâches, alertes] |
| Fourniture des données / code | [Nom] | [Livraison / accès] |
| Infrastructure / support technique | [Nom / service] | [Accès / maintenance] |

**Charge d'ingénierie envisagée :** [Jours ou personnes-mois ; estimation indicative et disponibilité]  
**Période et contraintes de calendrier :** [Dates, campagnes de mesure, publications, absences, etc.]

| Jalons | Échéance cible | Résultat observable |
|---|---|---|
| M0 — Pré requis levés | [Date] | [Accès, données et décision IA clarifiés] |
| M1 — Premier incrément / MVP | [Date] | [Démonstration ou résultat intermédiaire] |
| M2 — Validation | [Date] | [Tests et retour du porteur] |
| M3 — Transfert et clôture | [Date] | [Livrables, documentation, bilan] |

**Principaux risques et dépendances :**

| Risque / dépendance | Conséquence | Mesure de réduction | Responsable |
|---|---|---|---|
| [Ex. données indisponibles] | [Impact] | [Action] | [Nom] |
| [Ex. complexité technique sous-estimée] | [Impact] | [POC / réduction du périmètre] | [Nom] |

**Règle en cas d'évolution du périmètre :** [Qui décide ? Comment consigner l'arbitrage ?]

## 6. Modalités de collaboration et de suivi (10 min)

**Outil de suivi :** [Projet Jira + Epic / URL]  
**Dépôt et documentation technique :** [URL / droits d'accès]  
**Canal d'échange :** [Messagerie, liste de diffusion, etc.]  
**Cadence de suivi :** ☐ Toutes les 2 semaines ☐ Autre : [Préciser]  
**Participants et format des points de suivi :** [Noms / 30 min / démonstration si pertinente]  
**Modalité de validation des livrables :** [Qui valide, sur quelle base, sous quel délai ?]  
**Publication / partage / réutilisation :** [Dépôt public ou privé, licences, calendrier de diffusion]  
### 6.1 Pérennité et transfert après la fin du soutien

> Identifier explicitement qui prendra le relais **au-delà** des personnes-mois SequoIA. Un transfert non attribué est un risque à suivre, pas une responsabilité implicite des ingénieurs.

| Élément à reprendre | Responsable après soutien | Ressources / modalités de transfert | Statut |
|---|---|---|---|
| Dépôt, versions et corrections | [Équipe / nom] | [Droits, documentation, maintenance] | ☐ Confirmé ☐ À décider |
| Hébergement et comptes | [Équipe / service] | [Infrastructure, budget, facturation] | ☐ Confirmé ☐ À décider ☐ Sans objet |
| Données, accès et conformité | [Équipe / nom] | [Autorisations, renouvellements, suppression] | ☐ Confirmé ☐ À décider ☐ Sans objet |
| Exploitation et assistance utilisateurs | [Équipe / nom] | [Runbook, incidents, support] | ☐ Confirmé ☐ À décider ☐ Sans objet |

**Modalité de passation et jalon de transfert :** [Démonstration, dépôt, documentation, formation ; date].  
**Service maintenu au-delà du soutien ?** ☐ Oui, conditions définies ☐ Non, prototype livré ☐ À décider.  
**Responsable de la décision de pérennisation :** [Nom / service].

## 7. Décisions du kick-off et actions immédiates (5 min)

### 7.1 Journal des arbitrages et écarts par rapport à la demande

> **Ne pas dupliquer les sections 1–6.** Noter ici les décisions qui changent ou précisent substantiellement le cadrage prérempli, les désaccords et les validations encore requises. Les corrections mineures se font simplement dans la section concernée.

| Date | Sujet / section modifiée | Situation initiale → cadrage retenu | Décideur(s) | Statut |
|---|---|---|---|---|
| [Date] | [Ex. §2 : MVP] | [Demande/proposition → résultat convenu] | [Noms] | ☐ Validé ☐ En attente |
| [Date] | [Ex. §3 : prérequis] | [Risque identifié → condition de go/no-go] | [Noms] | ☐ Validé ☐ En attente |
| [Date] | [Ex. §4 : assistants IA] | [Options → autorisations et restrictions explicites] | [Noms/services] | ☐ Validé ☐ En attente |

### 7.2 Actions à suivre dans Jira

| Action | Responsable | Contributeur(s) | Échéance | Ticket Jira / lien |
|---|---|---|---|---|
| [Action à réaliser] | Ingénieur 1 | Ingénieur 2 |[Date] | [Lien à créer] |
| [Action à réaliser] | Ingénieur 2 |             |[Date] | [Lien à créer] |

**Questions ouvertes / décisions en attente :** [Point, personne chargée de trancher, échéance et effet sur le démarrage ou le pilote]  
**Prochaine réunion :** [Date / modalité]

## 8. Validation du cadrage

**Le périmètre, les livrables, les responsabilités, les prérequis de démarrage et les modalités de transfert après soutien ont-ils été confirmés ?**  
☐ Oui  ☐ Oui, avec réserves listées ci-dessus  ☐ Non — lancement différé

**Référent scientifique :** [Nom, date / confirmation]  
**Ingénieurs SequoIA :** [Nom, date / confirmation]

> **Après la réunion :** finaliser **ce même document**, dater et signaler les décisions validées (section 7), solliciter une confirmation écrite des responsables (section 8), puis créer l’Epic et les premiers tickets Jira. Les éléments non validés restent explicitement ouverts, avec responsable et échéance ; ils ne sont pas transformés en engagements implicites. Réviser la section IA si les données, les outils ou les règles changent.
