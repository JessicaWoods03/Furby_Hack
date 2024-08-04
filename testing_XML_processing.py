import pyspark
from lxml import etree
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext


# trouble shooting SparkConf bugs to create etrees in the wiki_dump_conf_save.py file

#this is added configurations of sparksession to see if this is the issue
# Define Spark configuration
# Initialize Spark session
# Initialize Spark configuration

# Create Spark session
from pyspark.sql import SparkSession

# Initialize Spark session with configurations
spark = SparkSession.builder.appName("XML Processing") \
    .config("spark.master", "local[42]") \
    .config("spark.executor.memory", "6g") \
    .config("spark.driver.memory","20g") \
    .config("spark.cores.max", "24") \
    .config("spark.default.parallelism", "24") \
    .config("spark.eventLog.enabled", "true") \
    .config("spark.eventLog.dir", "/tmp/spark-events") \
    .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.13.0") \
    .getOrCreate()

# Your code here...


Print("Spark session created successfully!")
spark.stop()
