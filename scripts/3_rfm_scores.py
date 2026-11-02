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


def calculate_rfm_scores():
  logger.info("⭐ Début de l'étape 3 : Attribution des scores RFM...")

  input_path = DATA_PROC / "rfm_raw.csv"
  output_path = DATA_PROC / "rfm_scores.csv"

  if not input_path.exists():
    logger.error(f"Fichier introuvable : {input_path}")
    sys.exit(1)

  try:
    rfm = pd.read_csv(input_path)

    rfm["R_Score"] = pd.qcut(
        rfm["Recency"], q=5, labels=[5, 4, 3, 2, 1], duplicates="drop"
    )
    rfm["F_Score"] = pd.qcut(
        rfm["Frequency"].rank(method="first"), q=5, labels=[1, 2, 3, 4, 5]
    )
    rfm["M_Score"] = pd.qcut(
        rfm["Monetary"], q=5, labels=[1, 2, 3, 4, 5], duplicates="drop"
    )

    rfm["R_Score"] = rfm["R_Score"].astype(int)
    rfm["F_Score"] = rfm["F_Score"].astype(int)
    rfm["M_Score"] = rfm["M_Score"].astype(int)

    rfm["RFM_Score_Str"] = (
        rfm["R_Score"].astype(str)
        + rfm["F_Score"].astype(str)
        + rfm["M_Score"].astype(str)
    )

    rfm.to_csv(output_path, index=False)
    logger.info(f"✅ Scores RFM sauvegardés dans : {output_path}")

  except Exception as e:
    logger.error(f"Erreur lors de l'attribution des quantiles : {e}")
    sys.exit(1)


if __name__ == "__main__":
  calculate_rfm_scores()