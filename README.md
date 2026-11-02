# 📊 Segmentation Client RFM & Analyse E-Commerce

Un pipeline complet de Data Analytics combinant **Python (Pandas)** pour le traitement des données et la modélisation RFM, et **Power BI** pour la création d'un tableau de bord décisionnel interactif.

---

## 📸 Aperçu du Tableau de Bord

![Aperçu du Tableau de Bord Power BI](./power_bi/dashboard_preview.png)

---

## 🎯 Contexte & Objectifs Business

Dans le secteur du e-commerce, l'acquisition de nouveaux clients coûte nettement plus cher que la fidélisation des clients existants. L'objectif de ce projet est de :

1. Nettoyer et transformer les données brutes de transactions e-commerce (`Online Retail Dataset`).
2. Calculer les métriques individuelles **RFM** :
   - **Récence (R) :** Nombre de jours depuis le dernier achat.
   - **Fréquence (F) :** Nombre total de commandes effectuées.
   - **Montant (M) :** Chiffre d'affaires total généré par le client.
3. Attribuer des scores de 1 à 5 (via quantiles) et catégoriser les clients en **segments stratégiques** (*Champions*, *Fidèles*, *À Risque*, *Perdus*, etc.). Les segments sont définis sur la base de R et F ; M est conservé en tant que valeur indépendante pour établir les priorités.
4. Concevoir un **tableau de bord décisionnel sur Power BI** pour permettre aux équipes marketing de piloter des campagnes ciblées.

---

## 🛠️ Stack Technique

- **Langage & Environnement :** Python 3.x | VS Code / Cursor
- **Analyse & Traitement de Données :** `pandas`, `numpy`, `openpyxl`
- **Data Visualization & BI :** Power BI Desktop, DAX (*Data Analysis Expressions*)
- **Gestion de Version :** Git & GitHub

---

## 📂 Structure & Pipeline du Projet

```text
rfm-customer-segmentation/
├── data/
│   ├── raw/                # Jeu de données d'origine
│   └── processed/          # Données nettoyées et tables RFM générées
├── scripts/                # Scripts Python de traitement et modélisation
├── power_bi/               # Rapport Power BI (.pbix) et visuels
├── .gitignore
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation du projet
🔄 Pipeline de Traitement des Données (Workflow)
Le traitement des données suit un flux séquentiel en 4 étapes clés :

[Données Brutes] ➡️ [1. Nettoyage] ➡️ [2. Calcul RFM] ➡️ [3. Scoring Quantiles] ➡️ [4. Segmentation] ➡️ [Power BI Dashboard]

🚀 Quickstart & Installation
Pour cloner et exécuter ce projet localement :

1. Cloner le dépôt :

Bash
git clone [https://github.com/votre-nom/rfm-customer-segmentation.git](https://github.com/votre-nom/rfm-customer-segmentation.git)
cd rfm-customer-segmentation
2. Créer et activer l'environnement virtuel :

Bash
python -m venv .venv
.venv\Scripts\activate          # Sous Windows (PowerShell)
# source .venv/bin/activate     # Sous Mac / Linux
3. Installer les dépendances :

Bash
pip install -r requirements.txt
4. Exécuter le pipeline séquentiellement :

Bash
python scripts/1_data_cleaning.py
python scripts/2_rfm_metrics.py
python scripts/3_rfm_scores.py
python scripts/4_segmentation.py
📈 Indicateurs Clés & Recommandations Business
💡 Principaux Enseignements (Key Insights) :
Règle des 80/20 (Loi de Pareto) : Le segment des Champions et des Clients Fidèles représente une minorité de la base client mais génère la majorité du chiffre d'affaires total.

Rétention Client : Identification d'un volume significatif de clients dans le segment À Risque, nécessitant des actions de réengagement urgentes avant leur passage définitif dans le segment Perdus.

🚀 Recommandations Marketing :
Champions : Programme VIP, accès anticipé aux nouveaux produits et récompenses exclusives.

Fidèles : Offres de surclassement (upselling) et programmes de parrainage.

À Risque / Requièrent de l'Attention : Campagnes d'emailing ciblées avec remises personnalisées pour stimuler le réachat.

✒️ Auteur
Fouzia Bakrim

Data Analyst


<FollowUp label="Veux-tu qu'on valide ensemble les commandes Git pour pousser cette version finale ?" quer