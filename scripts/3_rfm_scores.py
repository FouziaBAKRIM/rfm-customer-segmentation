import logging
from pathlib import Path
import pandera as pa
from pandera import Column, DataFrameSchema, Check
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

rfm_scores_schema = DataFrameSchema({
    "CustomerID": Column(int, nullable=False),
    "Recency": Column(int, Check.ge(0)),
    "Frequency": Column(int, Check.gt(0)),
    "Monetary": Column(float, Check.gt(0)),
    "R_Score": Column(int, Check.in_range(1, 5)),
    "F_Score": Column(int, Check.in_range(1, 5)),
    "M_Score": Column(int, Check.in_range(1, 5)),
    "RFM_Score_Str": Column(str, nullable=False),
})


def calculate_rfm_scores():
  logger.info("⭐ Étape 3 : Attribution et validation des scores RFM...")

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
    # Forcer la conversion en int propre pour éviter le conflit float64 de Pandas
    rfm["CustomerID"] = rfm["CustomerID"].astype(int)
    validated_scores = rfm_scores_schema.validate(rfm)
    validated_scores.to_csv(output_path, index=False)
    logger.info(f"✅ Scores RFM validés et sauvegardés dans : {output_path}")

  except pa.errors.SchemaError as e:
    logger.error(f"❌ Erreur de contrat sur les scores RFM : {e}")
    sys.exit(1)
  except Exception as e:
    logger.error(f"Erreur lors de l'attribution des scores : {e}")
    sys.exit(1)


if __name__ == "__main__":
  calculate_rfm_scores()