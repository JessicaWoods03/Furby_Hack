# so this saves multiple element trees into text files
# for testing the language model
import os
import logging
import pyspark
from lxml import etree
from pyspark.sql import SparkSession
from pyspark import SparkConf

print(pyspark.__version__)
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to parse XML row
def parse_xml(row):
    xml_string = row['value']
    root = etree.fromstring(xml_string.encode('utf-8'))
    title = root.find('{http://www.mediawiki.org/xml/export-0.11/}title').text
    text = root.find('{http://www.mediawiki.org/xml/export-0.11/}revision/{http://www.mediawiki.org/xml/export-0.11/}text').text
    return (title, text)

# Initialize Spark session
spark = SparkSession.builder.appName("XML Processing") \
    .config("spark.master", "local[24]") \
    .config("spark.executor.memory", "6g") \
    .config("spark.driver.memory", "20g") \
    .config("spark.cores.max", "24") \
    .config("spark.default.parrellelism", "24") \
    .config("spark.eventLog.enabled", "true") \
    .config("spark.eventLog.dir", "/tmp/spark-events") \
    .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.13.0") \
    .getOrCreate()

spark.conf.set("spark.sql.shuffle.partitions", "200")  # Default is 200; adjust if necessary

# Set the output directory where the chunks are stored
output_dir = '/home/jessica/Documents/xml_chunks'

# Dynamically collect chunk files for processing
chunk_files = [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith('.xml')]

# Process each chunk with Spark
for chunk_file in chunk_files:
    logger.info(f"Loading XML data from {chunk_file}...")
    xml_df = spark.read.format('xml').option("rowTag", "page").load(chunk_file)
    logger.info("XML data loaded successfully.")

    # Parse XML data
    logger.info("Parsing XML data...")
    parsed_data = xml_df.rdd.map(parse_xml).persist()

    # Example: Collect and print parsed data
    for title, text in parsed_data.collect():
        logger.info(f"Title: {title}")
        logger.info(f"Text: {text}")
        logger.info("")

    # Save parsed data to output file
    output_rdd = parsed_data.map(lambda x: f"Title: {x[0]}\nText: {x[1]}\n\n")
    output_file = os.path.join(output_dir, f'parsed_output_{os.path.basename(chunk_file).replace(".xml", "")}.txt')
    output_rdd.saveAsTextFile(output_file)
    logger.info(f"Parsed data saved successfully to {output_file}.")

# Stop Spark session
logger.info("Stopping Spark session...")
spark.stop()
logger.info("Spark session stopped.")
