import pandas as pd
# 1. Chargement des données
# Remplacez 'data.csv' par le nom exact de votre fichier CSV s'il est différent
print("Chargement du jeu de données...")
try:
    df = pd.read_csv('data.csv', encoding='ISO-8859-1')
except FileNotFoundError:
    print("Erreur : Fichier introuvable. Vérifiez le nom de votre fichier CSV.")
    exit()

print(f"Taille initiale du dataset : {df.shape[0]} lignes et {df.shape[1]} colonnes.\n")
# 2. Aperçu des données
print("--- Aperçu des 5 premières lignes ---")
print(df.head())
print("\n--- Informations sur les colonnes et types de données ---")
print(df.info())
# 3. Traitement des valeurs manquantes (Suppression des CustomerID nuls)
df_clean = df.dropna(subset=['CustomerID'])
print(f"\nLignes après suppression des CustomerID manquants : {len(df_clean)}")

# 4. Suppression des annulations (Invoices commençant par 'C' ou Quantités <= 0)
df_clean = df_clean[df_clean['Quantity'] > 0]

# 5. Suppression des prix unitaires absurdes (Prix <= 0)
df_clean = df_clean[df_clean['UnitPrice'] > 0]

# 6. Création de la colonne du Montant Total (TotalAmount)
df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']

# 7. Conversion de la colonne InvoiceDate au format Date/Heure
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])

# 8. Conversion de CustomerID en entier (pour enlever le .0 à la fin)
df_clean['CustomerID'] = df_clean['CustomerID'].astype(int)

# --- Bilan du nettoyage ---
print("\n" + "="*40)
print("NETTOYAGE TERMINÉ AVEC SUCCÈS !")
print("="*40)
print(f"Nombre de lignes conservées : {len(df_clean)}")
print(f"Nombre de lignes supprimées : {len(df) - len(df_clean)}")

# 9. Sauvegarde du fichier propre
df_clean.to_csv('data_clean.csv', index=False)
print("\nLe fichier nettoyé a été sauvegardé sous le nom 'data_clean.csv'.")