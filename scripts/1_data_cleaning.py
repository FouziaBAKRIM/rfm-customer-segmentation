import logging
from pathlib import Path
import sys
import pandas as pd

# Configuration du logging (horodatage + niveau de sévérité)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Chemins robustes basés sur pathlib
ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT / "data" / "raw"
DATA_PROC = ROOT / "data" / "processed"


def clean_data():
  logger.info("🧹 Début de l'étape 1 : Nettoyage des données...")

  input_path = DATA_RAW / "data.csv"
  output_path = DATA_PROC / "cleaned_data.csv"

  if not input_path.exists():
    logger.error(f"Fichier introuvable : {input_path}")
    sys.exit(1)

  DATA_PROC.mkdir(parents=True, exist_ok=True)

  try:
    df = pd.read_csv(input_path, encoding="ISO-8859-1")
  except Exception as e:
    logger.error(f"Erreur lors de la lecture du fichier CSV : {e}")
    sys.exit(1)

  df = df.dropna(subset=["CustomerID"])
  df = df.drop_duplicates()
  df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
  df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

  df.to_csv(output_path, index=False)
  logger.info(f"✅ Données nettoyées sauvegardées dans : {output_path}")


if __name__ == "__main__":
  clean_data()