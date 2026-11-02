import logging
from pathlib import Path
import sys
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
DATA_PROC = ROOT / "data" / "processed"


def calculate_rfm_metrics():
  logger.info("📊 Début de l'étape 2 : Calcul des métriques RFM brutes...")

  input_path = DATA_PROC / "cleaned_data.csv"
  output_path = DATA_PROC / "rfm_raw.csv"

  if not input_path.exists():
    logger.error(f"Fichier introuvable : {input_path}")
    sys.exit(1)

  try:
    df = pd.read_csv(input_path)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    rfm_df = (
        df.groupby("CustomerID")
        .agg({
            "InvoiceDate": lambda x: (
                snapshot_date - x.max()
            ).days,  # Récence
            "InvoiceNo": "nunique",  # Fréquence
            "TotalPrice": "sum",  # Montant
        })
        .reset_index()
    )

    rfm_df.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]
    rfm_df.to_csv(output_path, index=False)
    logger.info(f"✅ Métriques RFM brutes sauvegardées dans : {output_path}")

  except Exception as e:
    logger.error(f"Erreur lors du calcul des métriques RFM : {e}")
    sys.exit(1)


if __name__ == "__main__":
  calculate_rfm_metrics()