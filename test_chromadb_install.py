import chromadb
from pyspark.sql import SparkSession
from chromadb import Client

spark = SparkSession.builder.appName("ChromaDB with PySpark").getOrCreate()
print(chromadb.__version__)

client = Client()
print("ChromaDB Client created successfully, in pyspark_env!")
collection = client.create_collection("example_collection")
documents = ["Hello World"]
ids = ["1"]
collection.add(documents=documents, ids=ids)

# check data has been added
data = collection.get()
print("Data in ChromaDB:", data)
spark.stop()
