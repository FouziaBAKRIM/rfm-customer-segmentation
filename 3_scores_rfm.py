import pandas as pd

# 1. Chargement des métriques RFM
rfm = pd.read_csv('rfm_metrics.csv', index_col='CustomerID')

print("Calcul des scores RFM de 1 à 5...")

# 2. Score de Récence (R_Score)
# Inversé : plus le nombre de jours est petit, plus le score est grand ( labels=[5, 4, 3, 2, 1] )
rfm['R_Score'] = pd.qcut(rfm['Recency'], q=5, labels=[5, 4, 3, 2, 1])

# 3. Score de Fréquence (F_Score)
# Si les valeurs sont très répétitives, rank(method='first') évite les erreurs de découpage
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5])

# 4. Score de Montant (M_Score)
rfm['M_Score'] = pd.qcut(rfm['Monetary'], q=5, labels=[1, 2, 3, 4, 5])

# Conversion des colonnes de score en entiers
rfm['R_Score'] = rfm['R_Score'].astype(int)
rfm['F_Score'] = rfm['F_Score'].astype(int)
rfm['M_Score'] = rfm['M_Score'].astype(int)

# 5. Calcul de la chaîne RFM (ex: '555', '111') et du Score Total RFM (ex: 15)
rfm['RFM_Group'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
rfm['RFM_Score'] = rfm['R_Score'] + rfm['F_Score'] + rfm['M_Score']

print("\n--- Aperçu des scores attribués aux clients ---")
print(rfm[['Recency', 'Frequency', 'Monetary', 'RFM_Group', 'RFM_Score']].head(10))

# 6. Sauvegarde du fichier final avec les scores
rfm.to_csv('rfm_scores.csv')
print("\nLe fichier contenant les scores RFM a été sauvegardé sous le nom 'rfm_scores.csv'.")