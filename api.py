import os
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# PySpark
from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.feature import VectorAssembler

# Configuration Python Spark
PYTHON = r"C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\python.exe"
os.environ["PYSPARK_PYTHON"] = PYTHON
os.environ["PYSPARK_DRIVER_PYTHON"] = PYTHON

# Spark session
spark = SparkSession.builder \
    .appName("ServeurAPI_Spark") \
    .getOrCreate()

# Vérification modèle
if not os.path.exists("modele_vol_retard"):
    raise Exception("❌ Modèle introuvable !")

modele_ia = LogisticRegressionModel.load("modele_vol_retard")

# Schéma des données
class DonneesVol(BaseModel):
    age_pilote: int
    distance_km: float

# API
app = FastAPI(
    title="API Prédiction Retard Vol ✈️",
    description="API utilisant Spark ML pour prédire les retards",
    version="1.0.0",
    contact={
        "name": "Yassine Missaoui",
        "email": "yassine@email.com",
        "url": "https://www.linkedin.com/in/yassine-missaoui-b4710335b/"
    }
)

# Route accueil
@app.get("/")
def page_accueil():
    return {"message": "Bienvenue sur mon API IA 🚀"}

# Route prédiction
@app.post("/predictions")
def faire_prediction(vol: DonneesVol):
    
    donnees_recues = [(vol.age_pilote, vol.distance_km)]
    
    df_vol = spark.createDataFrame(
        donnees_recues, 
        ["age_pilote", "distance_km"]
    )
    
    assembleur = VectorAssembler(
        inputCols=["age_pilote", "distance_km"], 
        outputCol='features'
    )
    
    df_features = assembleur.transform(df_vol)
    
    prediction_df = modele_ia.transform(df_features)
    
    resultat_final = prediction_df.collect()[0]["prediction"]
    
    return {
        "statut": "succès",
        "age_pilote": vol.age_pilote,
        "distance_km": vol.distance_km,
        "prediction_retard": int(resultat_final)
    }

# Lancement serveur
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)