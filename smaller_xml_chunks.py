import os
from lxml import etree
from pyspark.sql import SparkSession

# Initialize Spark session with configurations
spark = SparkSession.builder.appName("XML Processing") \
    .config("spark.master", "local[24]") \
    .config("spark.executor.memory", "10g") \
    .config("spark.driver.memory", "20g") \
    .config("spark.sql.files.maxPartitionBytes", "128MB") \
    .config("spark.eventLog.dir", "/tmp/spark-events") \
    .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.13.0") \
    .getOrCreate()

# Maximum size for each chunk (in bytes)
MAX_SIZE = 1000000000  # 1GB size limit for each chunk
current_size = 0

# File paths
input_file = "/home/jessica/Documents/xml_chunks/chunk_0.xml"
output_dir = "/home/jessica/Documents/xml_chunks"  # Directory where the chunks will be saved

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parse the large XML file
context = etree.iterparse(input_file, events=("start", "end"))

# Initialize variables for output
current_chunk = 1
output_file = None
current_writer = None
namespace_subject = None
namespace_subject_files = {}  # To track the files for each namespace_subject combination

# Function to start a new chunk file
def start_new_chunk(namespace_subject, chunk_counter):
    global output_file, current_writer
    output_file = os.path.join(output_dir, f"{namespace_subject}_{chunk_counter}.xml")
    
    # Start the new chunk file with the XML declaration and <mediawiki> tag
    with open(output_file, "wb") as out_f:
        out_f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        out_f.write(b'<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/">\n')
    
    # Open for appending to the current file
    current_writer = open(output_file, 'ab')

# Function to close the current chunk
def close_current_chunk():
    global current_writer
    if current_writer:
        current_writer.write(b"</mediawiki>\n")
        current_writer.close()
        current_writer = None  # Reset to None after closing

# Iterate through the XML elements
for event, element in context:
    if event == "start" and element.tag == "{http://www.mediawiki.org/xml/export-0.11/}page":
        title_element = element.find("{http://www.mediawiki.org/xml/export-0.11/}title")
        if title_element is not None:
            title_text = title_element.text
            if '/' in title_text:
                namespace, subject = title_text.split('/', 1)
            else:
                namespace, subject = title_text, ""

            # Sanitize the subject for filenames
            namespace_subject_new = f"{namespace}_{subject.replace('/', '_')}"

            # Check if we need to start a new chunk (based on namespace_subject)
            if namespace_subject != namespace_subject_new or current_writer is None:
                # Close the current chunk if it exists
                if current_writer is not None:
                    close_current_chunk()

                # Update the namespace_subject
                namespace_subject = namespace_subject_new

                # Check if a file for this namespace_subject exists, and determine chunk file number
                if namespace_subject not in namespace_subject_files:
                    namespace_subject_files[namespace_subject] = 1
                else:
                    namespace_subject_files[namespace_subject] += 1

                # Start a new chunk for the new namespace_subject
                start_new_chunk(namespace_subject, namespace_subject_files[namespace_subject])
                current_size = 0  # Reset size for the new chunk

            # Calculate the size of this page element
            page_size = len(etree.tostring(element, pretty_print=True))

            # Check if adding this page exceeds the max size
            if current_size + page_size > MAX_SIZE:
                # Close the current chunk and start a new one
                close_current_chunk()
                namespace_subject_files[namespace_subject] += 1  # Increment the chunk file counter
                start_new_chunk(namespace_subject, namespace_subject_files[namespace_subject])
                current_size = 0  # Reset size for the new chunk

            # Add the current page to the current chunk file
            current_writer.write(etree.tostring(element, pretty_print=True))
            current_size += page_size

    # Clear the element to save memory
    element.clear()

# Close the last chunk with </mediawiki>
close_current_chunk()

print(f"Splitting complete. Files saved in {output_dir}.")

# Stop Spark session
spark.stop()
