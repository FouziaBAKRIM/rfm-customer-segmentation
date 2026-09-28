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
3. Attribuer des scores de 1 à 5 (via quantiles) et catégoriser les clients en **segments stratégiques** (*Champions*, *Fidèles*, *À Risque*, *Perdus*, etc.).
4. Concevoir un **tableau de bord décisionnel sur Power BI** pour permettre aux équipes marketing de piloter des campagnes ciblées.

---

## 🛠️ Stack Technique

- **Langage & Environnement :** Python 3.x | VS Code
- **Analyse & Traitement de Données :** `pandas`, `numpy`, `openpyxl`
- **Data Visualization & BI :** Power BI Desktop, DAX (*Data Analysis Expressions*)
- **Gestion de Version :** Git & GitHub

---

## 🔄 Pipeline de Données & Architecture du Projet

├── data/
│   ├── raw/                 # Données brutes d'origine
│   ├── data_clean.csv       # Données nettoyées (valeurs manquantes et retours traités)
│   ├── rfm_metrics.csv      # Métriques brutes R, F, M calculées par client
│   ├── rfm_scores.csv       # Scores RFM (1 à 5)
│   └── rfm_segmented.csv    # Segments finaux attribués
├── scripts/
│   ├── 1_data_cleaning.py   # Nettoyage des données et filtrage
│   ├── 2_rfm_metrics.py     # Calcul des valeurs R, F, M
│   ├── 3_rfm_scores.py      # Découpage en quantiles (Scores 1-5)
│   └── 4_segmentation.py    # Cartographie des segments business
├── power_bi/
│   ├── RFM_Customer_Segmentation.pbix
│   └── dashboard_preview.png
└── README.md
---

## 📈 Indicateurs Clés & Recommandations Business

### 💡 Principaux Enseignements (Key Insights) :
- **Règle des 80/20 (Loi de Pareto) :** Le segment des **Champions** et des **Clients Fidèles** représente une minorité de la base client mais génère la majorité du chiffre d'affaires total.
- **Rétention Client :** Identification d'un volume significatif de clients dans le segment **À Risque**, nécessitant des actions de réengagement urgentes avant leur passage définitif dans le segment **Perdus**.

### 🚀 Recommandations Marketing :
1. **Champions :** Programme VIP, accès anticipé aux nouveaux produits et récompenses exclusives.
2. **Fidèles :** Offres de surclassement (*upselling*) et programmes de parrainage.
3. **À Risque / Requièrent de l'Attention :** Campagnes d'emailing ciblées avec remises personnalisées pour stimuler le réachat.

---

## ✒️ Auteur

**[BAKRIM / Fouzia]**  
*Data Analyst* — [Profil LinkedIn](https://linkedin.com/in/fouzia-bakrim-204872210)