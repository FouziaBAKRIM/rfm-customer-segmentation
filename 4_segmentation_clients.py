import pandas as pd

# 1. Chargement des scores RFM
rfm = pd.read_csv('rfm_scores.csv', index_col='CustomerID')

# 2. Fonction de correspondance pour attribuer un segment
def assign_segment(df):
    r = df['R_Score']
    f = df['F_Score']
    
    if r >= 4 and f >= 4:
        return 'Champions'
    elif r >= 3 and f >= 3:
        return 'Clients Fideles'
    elif r >= 4 and f <= 2:
        return 'Nouveaux / Potentiels'
    elif r <= 2 and f >= 3:
        return 'A Risque'
    elif r == 3 and f == 3:
        return 'Nécessitent Attention'
    else:
        return 'Perdus / Inactifs'

# 3. Application de la fonction
print("Application des règles de segmentation...")
rfm['Segment'] = rfm.apply(assign_segment, axis=1)

# 4. Analyse de la répartition des clients par segment
print("\n--- Répartition des clients par Segment ---")
segment_counts = rfm['Segment'].value_counts()
print(segment_counts)

print("\n--- Pourcentage de clients par Segment ---")
segment_perc = rfm['Segment'].value_counts(normalize=True) * 100
print(segment_perc.round(2).astype(str) + ' %')

# 5. Calcul des métriques moyennes par segment (pour vérifier la cohérence)
print("\n--- Moyennes (Recency, Frequency, Monetary) par Segment ---")
segment_summary = rfm.groupby('Segment').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': ['mean', 'count']
}).round(2)
print(segment_summary)

# 6. Sauvegarde du fichier final segmenté
rfm.to_csv('rfm_segmented.csv')
rfm.to_excel('rfm_segmented.xlsx') # Également en Excel pour l'intégration Power BI
print("\nLe fichier final a été sauvegardé sous 'rfm_segmented.csv' et 'rfm_segmented.xlsx'.")