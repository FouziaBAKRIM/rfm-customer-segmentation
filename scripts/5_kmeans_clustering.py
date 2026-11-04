import logging
from pathlib import Path
import pandera.pandas as pa
from pandera import Check, Column, DataFrameSchema
import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
DATA_PROC = ROOT / "data" / "processed"

# Schéma Pandera enrichi : il valide les segments métiers ET le cluster K-Means dans le même fichier
kmeans_schema = DataFrameSchema({
    "CustomerID": Column(int, nullable=False),
    "Recency": Column(int, Check.ge(0)),
    "Frequency": Column(int, Check.gt(0)),
    "Monetary": Column(float, Check.gt(0)),
    "Segment": Column(str, nullable=False),
    "Cluster": Column("int64", Check.in_range(0, 3)),
})

def apply_kmeans_clustering():
    logger.info("🤖 Étape 5 : Clustering K-Means et fusion avec les segments finaux...")

    # On charge directement le fichier final de l'étape 4
    input_path = DATA_PROC / "final_rfm_segments.csv"

    if not input_path.exists():
        logger.error(f"❌ Fichier introuvable : {input_path}")
        sys.exit(1)

    try:
        rfm = pd.read_csv(input_path)
        rfm["CustomerID"] = rfm["CustomerID"].astype(int)

        # Extraction des features pour le K-Means
        X = rfm[["Recency", "Frequency", "Monetary"]]
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Application du K-Means (4 clusters)
        kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
        rfm["Cluster"] = kmeans.fit_predict(X_scaled)
        rfm["Cluster"] = rfm["Cluster"].astype("int64")

        # Validation par contrat Pandera sur le dataframe enrichi
        validated_df = kmeans_schema.validate(rfm)

        # On sauvegarde directement dans le fichier final pour Power BI
        validated_df.to_csv(input_path, index=False)
        logger.info(f"✅ K-Means fusionné et validé avec succès dans : {input_path}")

    except pa.errors.SchemaError as e:
        logger.error(f"❌ Erreur de contrat Pandera (K-Means) : {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Erreur lors de l'exécution du K-Means : {e}")
        sys.exit(1)

if __name__ == "__main__":
    apply_kmeans_clustering()