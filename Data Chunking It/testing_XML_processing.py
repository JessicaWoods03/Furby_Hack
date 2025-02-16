import pyspark
from lxml import etree
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col, split
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
    .config("spark.executor.memory", "10g") \
    .config("spark.driver.memory","20g") \
    .config("spark.sql.files.maxPartitionBytes", "128MB") \
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
    
with open(chunk_file, 'r') as f:
    print(f.read(200))  # prints first 200 characters of the file

# Process each chunk with Spark
xml_df = spark.read.format('xml').option("rowTag", "page").load(chunk_file)
print(f"XML data loaded from {chunk_file}")
# test namespace splitting before I run it threw the wiki_dump_config_save.py file
xml_df.printSchema()
xml_df.show(5, truncate=False)

# Extract Namespace
#xml_df_with_namespace = xml_df.withColumn('namespace', split(col('page.title'), ':').getItem(0))

# Show the schema to verify the extraction
#xml_df_with_namespace.printSchema()
# show rows
#xml_df_with_namespace.select("page.title", "namespace").show(5)

#show specific namespace like Afghanistan
#namespace = "Afghanistan"
#namespace_df = xml_df_with_namespace.filter(xml_df_with_namespace["namespace"] == namespace)

# show filtered data
#namespace_df.show(5)

# Print titles and namespace to verify that it works

print("Titles and Namespaces")
#for row in xml_df_with_namespace.collect():
    #print(f"Title: {row['title']}, Namespace: {row['namespace']}")


# root = xml_df.
# Stop Spark session
print("Spark session created successfully!")
spark.stop()

#finally works
# using bash command $ spark-submit \
# --conf "spark.eventLog.enabled=true" \
# --conf "spark.eventLog.dir=/tmp/spark-events" \
# --packages com.databricks:spark-xml_2.12:0.13.0 \
#  testing_XML_processing.py

# adjusting bash command
# --conf "spark.executor.extraJavaOptions=-XX:+UseG1GC -XX:MaxGCPauseMillis=200"
# --conf "spark.driver.extraJavaOptions=-XX:+UseG1GC -XX:MaxGCPauseMillis=200"
# --conf "spark.dynamicAllocation.enabled=true" \
# --conf "spark.dynamicAllocation.minExecutors=1" \
# --conf "spark.dynamicAllocation.maxExecutors=10" \
# --conf "spark.dynamicAllocation.initialExecutors=4"
# --conf "spark.executor.memory=10g"   --conf "spark.executor.cores=4"   --conf "spark.driver.memory=10g"
# --conf "spark.sql.shuffle.partitions=200"   --conf "spark.eventLog.enabled=true"   --conf "spark.eventLog.dir=/tmp/spark-events"
# --packages com.databricks:spark-xml_2.12:0.13.0   testing_XML_processing.py



