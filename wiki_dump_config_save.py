# handling xml parsing from wiki dump
# https://dumps.wikimedia.org/enwiki/20240701/
# file = enwiki-20240701-pages-meta-history1.xml-p1p812.bz2 36.6 GB
# file = enwiki-20240701-pages-meta-history1.xml-p813p1460.bz2 36.6 GB
# using emacs editor

from lxml import etree
# using pyspark
from pyspark.sql import SparkSession
import logging
from pyspark import SparkConf

# ran into memory issues due to the file being really big
# this will help with memory allowcations
# can also do this in bash commands, but my bash is already complicated enough, incase I need to adjust this its
# best to just have it here.
conf = SparkConf() \
    .set("spark.sql.shuffle.partitions", "200") \
    .set("spark.default.parallelism", "200") \
    .set("spark.executor.memory", "4g") \
    .set("spark.driver.memory", "4g")



# configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#initialize spark
logger.info("Start Spark session..")
spark = SparkSession.builder.appName("XML Processing").config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.13.0").getOrCreate()

# fingers crossed, load XML
logger.info("Loading XML data...")

# move this down to smaller sizes of chunks to do to adjust for the memory issues in java.lang.OutOfMemoryError
xml_df = spark.read.format('xml').option("rowTag", "page").load('/home/jessica/Documents/enwiki-20240701-pages-meta-history1.xml')
logger.info("XML data loaded successfully.")
# use bash :spark-submit --packages com.databricks:spark-xml_2.12:0.13.0 wiki_dump_config_save.py

# xml parsing
def parse_xml(row):
    xml_string = row['value']
    root = etree.fromstring(xml_string.encode('utf-8'))
    title = root.find('title').text
    text = root.find('revision/text').text
    return (title, text)

# Apply parsing function to each row in DataFrame
# want to use persist() or catch() so it helps with memory
logger.info("Parsing XML data...")
parsed_data = xml_df.rdd.map(parse_xml).persist()

# Example: Collect and print parsed data
for title, text in parsed_data.collect():
    logger.info(f"Title: {title}")
    logger.info(f"Text: {text}")
    logger.info("")

logger.info("Saving parsed data to output.txt")
output_rdd = parsed_data.map(lambda x: f"Title: {x[0]}\nText: {x[1]}\n\n")
output_rdd.saveAsTextFile('parsed_output.txt')
logger.info("Parsed data saved successfully.")

# Stop Spark session
logger.info("Stopping Spark session...")
spark.stop()
logger.info("Spark session stopped.")

