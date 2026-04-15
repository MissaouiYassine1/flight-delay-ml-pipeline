import os

PYTHON = r"C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\python.exe"

os.environ["PYSPARK_PYTHON"] = PYTHON
os.environ["PYSPARK_DRIVER_PYTHON"] = PYTHON

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
spark = SparkSession.builder \
    .appName("MonPremierProjetBigData") \
    .getOrCreate()

data = [
    (1, "Sfax", 0),
    (2, "Kasserine", 1),
    (3, "Kef", 3),
    (4, "Tunis", 5)
]

cols = ["id_vol", "ville_depart", "retard_minutes"]

df = spark.createDataFrame(data, cols)

df.show()
print(df.count())


df_filtre = df.filter(df['retard_minutes']>0)

df_filtre.show()

df = df.withColumn("retard_heures",df['retard_minutes'] / 60)

df.show()

data = df.groupBy('ville_depart').agg(F.max('retard_minutes').alias('retard_max'))

data.show()
input("donner quelques chose...")