import pyspark
from lxml import etree
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext


# trouble shooting SparkConf bugs to create etrees in the wiki_dump_conf_save.py file

#this is added configurations of sparksession to see if this is the issue
# Define Spark configuration
# Initialize Spark session
spark = SparkSession.builder \
    .appName("XML Processing") \
    .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.13.0") \
    .getOrCreate()



Print("Spark session created successfully!")
spark.stop()
