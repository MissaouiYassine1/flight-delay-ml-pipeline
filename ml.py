import os

PYTHON = r"C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\python.exe"

os.environ["PYSPARK_PYTHON"] = PYTHON
os.environ["PYSPARK_DRIVER_PYTHON"] = PYTHON

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
spark = SparkSession.builder \
    .appName("MonPremierProjetBigData") \
    .getOrCreate()



from pyspark.ml.feature import VectorAssembler

# On crée des données numériques pour le ML
data_ml = [
    (1, 40, 1500, 0), # id_vol, age_pilote, distance_km, cible_retard
    (2, 55, 2000, 1),
    (3, 30, 800,  0),
    (4, 45, 3000, 1)
]
cols_ml = ["id_vol", "age_pilote", "distance_km", "cible_retard"]
df_ml = spark.createDataFrame(data_ml, cols_ml)

assembleur = VectorAssembler(inputCols=["age_pilote", "distance_km"],outputCol='features')

df_prepare = assembleur.transform(df_ml)

df_prepare.show()


from pyspark.ml.classification import LogisticRegression

# 1. Séparation des données (on met un seed pour que l'aléatoire soit le même pour nous deux)
train_data, test_data = df_prepare.randomSplit([0.7, 0.3], seed=42)

# 2. Initialisation de l'algorithme
# MISSION A : Crée une variable nommée 'algo' en utilisant LogisticRegression. 
# Tu dois lui passer deux paramètres : featuresCol="features" et labelCol="cible_retard"

algo = LogisticRegression(featuresCol='features', labelCol='cible_retard')

# 3. L'apprentissage
# MISSION B : Crée une variable 'modele' en appliquant la méthode .fit(train_data) sur ton 'algo'

modele = algo.fit(train_data)

# 4. La prédiction
# MISSION C : Crée un DataFrame 'predictions' en appliquant la méthode .transform(test_data) sur ton 'modele'

predictions = modele.transform(test_data)

# MISSION D : Affiche les données de 'predictions' avec .show()
# Observe bien les nouvelles colonnes générées à la fin du tableau (rawPrediction, probability, prediction) !

predictions.show()


# On sauvegarde le cerveau entraîné dans un dossier nommé "modele_vol_retard"
modele.write().overwrite().save("modele_vol_retard")
print("✅ Modèle sauvegardé avec succès sur le disque dur !")

input("Appuyez sur Entrée pour quitter...")