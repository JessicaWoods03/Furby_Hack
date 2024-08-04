import pyspark
from lxml import etree
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
import os

# trouble shooting SparkConf bugs to create etrees in the wiki_dump_conf_save.py file

#this is added configurations of sparksession to see if this is the issue
# Define Spark configuration
# Initialize Spark session
# Initialize Spark configuration

# Create Spark session
from pyspark.sql import SparkSession

# Initialize Spark session with configurations
spark = SparkSession.builder.appName("XML Processing") \
    .config("spark.master", "local[24]") \
    .config("spark.executor.memory", "6g") \
    .config("spark.driver.memory","20g") \
    .config("spark.eventLog.dir", "/tmp/spark-events") \
    .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.13.0") \
    .getOrCreate()

# Directory containing XML files
output_dir = '/home/jessica/Documents/xml_chunks'

# Dynamically collect chunk files for processing
chunk_file = "/home/jessica/Documents/xml_chunks/chunk_0.xml"

if os.path.exists(chunk_file):
    print(f"File exists: {chunk_file}")
else:
    print(f"File does not exist: {chunk_file}")

# Process each chunk with Spark
xml_df = spark.read.format('xml').option("rowTag", "article").load(chunk_file)


# Stop Spark session
Print("Spark session created successfully!")
spark.stop()

#finally works
# using bash command $ spark-submit \
# --conf "spark.eventLog.enabled=true" \
# --conf "spark.eventLog.dir=/tmp/spark-events" \
# --packages com.databricks:spark-xml_2.12:0.13.0 \
#  testing_XML_processing.py
