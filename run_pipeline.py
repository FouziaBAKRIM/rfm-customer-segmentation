import importlib
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

ROOT = Path(__file__).resolve().parent
DATA_RAW = ROOT / "data" / "raw"
DATA_PROC = ROOT / "data" / "processed"


def run_full_pipeline():
  logger.info(
      "🚀 Démarrage du pipeline RFM & K-Means complet (Noms d'origine)..."
  )

  raw_file = DATA_RAW / "data.csv"
  if not raw_file.exists():
    logger.error(
        f"❌ Erreur critique : Fichier de données brutes introuvable à"
        f" {raw_file}"
    )
    sys.exit(1)

  try:
    # 🔄 Chargement dynamique avec les noms d'origine exacts
    step1 = importlib.import_module("scripts.1_data_cleaning")
    step2 = importlib.import_module("scripts.2_rfm_metrics")
    step3 = importlib.import_module("scripts.3_rfm_scores")
    step4 = importlib.import_module("scripts.4_segmentation")
    step5 = importlib.import_module("scripts.5_kmeans_clustering")

    # Exécution séquentielle des 5 étapes
    step1.clean_data()
    step2.calculate_rfm_metrics()
    step3.calculate_rfm_scores()
    step4.segment_customers()
    step5.apply_kmeans_clustering()

  except Exception as e:
    logger.error(f"❌ Erreur lors de l'exécution d'une étape du pipeline : {e}")
    sys.exit(1)

  # 📊 Rapport de fin d'exécution (Run Summary)
  logger.info("📋 Génération du rapport de fin d'exécution (Run Summary)...")

  try:
    raw_df = pd.read_csv(raw_file, encoding="ISO-8859-1")
    cleaned_df = pd.read_csv(DATA_PROC / "cleaned_data.csv")
    rfm_raw_df = pd.read_csv(DATA_PROC / "rfm_raw.csv")
    final_df = pd.read_csv(DATA_PROC / "final_rfm_segments.csv")
    kmeans_df = pd.read_csv(DATA_PROC / "rfm_kmeans_segments.csv")

    cleaned_df["InvoiceDate"] = pd.to_datetime(cleaned_df["InvoiceDate"])
    min_date = cleaned_df["InvoiceDate"].min().strftime("%Y-%m-%d")
    max_date = cleaned_df["InvoiceDate"].max().strftime("%Y-%m-%d")
    snapshot_date = (
        cleaned_df["InvoiceDate"].max() + pd.Timedelta(days=1)
    ).strftime("%Y-%m-%d")

    print("\n" + "=" * 50)
    print("📊 RAPPORT D'EXÉCUTION DU PIPELINE (RUN SUMMARY)")
    print("=" * 50)
    print(f"• Lignes en entrée (Raw)      : {len(raw_df):,}")
    print(f"• Lignes en sortie (Cleaned)  : {len(cleaned_df):,}")
    print(f"• Nombre total de clients     : {len(rfm_raw_df):,}")
    print(f"• Plage de dates des factures : Du {min_date} au {max_date}")
    print(f"• Date de snapshot (Référence): {snapshot_date}")
    print(f"• Segments métiers identifiés : {final_df['Segment'].nunique()}")
    print(f"• Clusters K-Means générés    : {kmeans_df['Cluster'].nunique()}")
    print("=" * 50)
    print("✅ Pipeline exécuté avec succès de bout en bout !")
    print("=" * 50 + "\n")

  except Exception as e:
    logger.error(f"Erreur lors de la génération du Run Summary : {e}")
    sys.exit(1)


if __name__ == "__main__":
  run_full_pipeline()