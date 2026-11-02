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
3. Attribuer des scores de 1 à 5 (via quantiles) et catégoriser les clients en **segments stratégiques** (*Champions*, *Fidèles*, *À Risque*, *Perdus*, etc.). Les segments sont définis sur la base de R et F ; M est conservé en tant que niveau de valeur indépendant, servant à établir des priorités au sein de chaque segment.
4. Concevoir un **tableau de bord décisionnel sur Power BI** pour permettre aux équipes marketing de piloter des campagnes ciblées.

---

## 🛠️ Stack Technique

- **Langage & Environnement :** Python 3.x | VS Code
- **Analyse & Traitement de Données :** `pandas`, `numpy`, `openpyxl`
- **Data Visualization & BI :** Power BI Desktop, DAX (*Data Analysis Expressions*)
- **Gestion de Version :** Git & GitHub

---

## 🔄 Pipeline de Données & Architecture du Projet

---

## 📂 Structure du Projet

```text
rfm-customer-segmentation/
├── data/
│   ├── raw/                  # Jeu de données d'origine
│   └── processed/            # Données nettoyées et tables RFM générées
├── scripts/                  # Scripts Python de traitement et modélisation
├── power_bi/                 # Rapport Power BI (.pbix) et visuels
├── .gitignore
├── requirements.txt          # Dépendances Python
└── README.md                 # Documentation du projet

🔄 Pipeline de Traitement des Données (Workflow)
Le traitement des données suit un flux séquentiel en 4 étapes clés :
[Données Brutes] ➡️ [1. Nettoyage] ➡️ [2. Calcul RFM] ➡️ [3. Scoring Quantiles] ➡️ [4. Segmentation] ➡️ [Power BI Dashboard]


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
```