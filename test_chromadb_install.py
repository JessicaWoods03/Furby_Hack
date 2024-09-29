import chromadb
from pyspark.sql import SparkSession
from chromadb import Client

spark = SparkSession.builder.appName("ChromaDB with PySpark").getOrCreate()
print(chromadb.__version__)

client = Client()
print("ChromaDB Client created successfully, in pyspark_env!")
spark.stop()
