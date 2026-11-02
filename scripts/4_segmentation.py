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


def segment_customers():
  logger.info("🎯 Début de l'étape 4 : Segmentation marketing des clients...")

  input_path = DATA_PROC / "rfm_scores.csv"
  output_path = DATA_PROC / "final_rfm_segments.csv"

  if not input_path.exists():
    logger.error(f"Fichier introuvable : {input_path}")
    sys.exit(1)

  try:
    rfm = pd.read_csv(input_path)

    def rfm_segment(row):
      r = row["R_Score"]
      f = row["F_Score"]

      if r >= 4 and f >= 4:
        return "Champions"
      elif r >= 3 and f >= 3:
        return "Fidèles"
      elif r >= 4 and f <= 2:
        return "Nouveaux / Prometteurs"
      elif r <= 2 and f >= 4:
        return "À Risque (Loyaux perdus)"
      elif r <= 2 and f <= 2:
        return "Perdus"
      else:
        return "Clients Réguliers"

    rfm["Segment"] = rfm.apply(rfm_segment, axis=1)
    rfm.to_csv(output_path, index=False)
    logger.info(
        f"✅ Segmentation terminée ! Fichier final prêt pour Power BI :"
        f" {output_path}"
    )

  except Exception as e:
    logger.error(f"Erreur lors de la segmentation : {e}")
    sys.exit(1)


if __name__ == "__main__":
  segment_customers()