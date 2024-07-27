from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("Example") \
    .getOrCreate()

# Create a DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
df = spark.createDataFrame(data, ["Name", "Id"])

# Show the DataFrame
df.show()

# Stop the Spark session
spark.stop()
# this just tested spark configurations on emacs
# bash command spark-submit spark_example.py on linux
