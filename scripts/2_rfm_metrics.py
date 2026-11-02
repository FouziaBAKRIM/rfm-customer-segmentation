import pandas as pd
import datetime as dt

# 1. Chargement des données nettoyées
print("Chargement des données nettoyées...")
df = pd.read_csv('data_clean.csv')

# Conversion de la colonne InvoiceDate en type Datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 2. Définir une date de référence pour calculer la récence
# On prend le jour suivant la transaction la plus récente du jeu de données
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
print(f"Date de référence pour le calcul : {snapshot_date.date()}")

# 3. Agrégation par client pour calculer R, F et M
print("\nCalcul des métriques RFM par client...")
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Récence (en jours)
    'InvoiceNo': 'nunique',                                   # Fréquence (nombre de factures uniques)
    'TotalAmount': 'sum'                                      # Montant total dépensé
})

# Renommer les colonnes pour plus de clarté
rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalAmount': 'Monetary'
}, inplace=True)

# 4. Aperçu du résultat
print("\n--- Aperçu des métriques RFM (5 premiers clients) ---")
print(rfm.head())

print("\n--- Statistiques descriptives du tableau RFM ---")
print(rfm.describe())

# 5. Sauvegarde du tableau RFM
rfm.to_csv('rfm_metrics.csv')
print("\nLe fichier des métriques RFM a été sauvegardé sous le nom 'rfm_metrics.csv'.")