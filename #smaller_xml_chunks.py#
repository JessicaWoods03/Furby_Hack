import os
from lxml import etree
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

# Maximum size for each chunk (in bytes)
MAX_SIZE = 1000000000  # 1GB size limit for each chunk
current_size = 0

# File paths
input_file = "/home/jessica/Documents/xml_chunks/chunk_0.xml"
output_dir = " /home/jessica/Documents/output_chunks"  # Directory where the chunks will be saved

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



# Parse the large XML file
context = etree.iterparse(input_file, events=("start", "end"))

# Initialize variables

namespace_subject = None  
output_file = None  
file_counter = 1  # Counter to generate file suffixes (e.g., _1.xml, _2.xml)

# Start processing the XML file
for event, element in context:
    if event == "start" and element.tag == "{http://www.mediawiki.org/xml/export-0.11/}page":
        # Start of a <page> element
        title_element = element.find("{http://www.mediawiki.org/xml/export-0.11/}title")
        if title_element is not None:
            # Extract the namespace and subject from the title (separate by '/')
            namespace, subject = title_element.text.split('/', 1)  # Split at the first '/'
            namespace_subject = f"{namespace}_{subject.replace('/', '_')}"  # Combine namespace and subject

        # Set output filename based on the namespace_subject and file_counter
        if namespace_subject:
            output_file = os.path.join(output_dir, f"{namespace_subject}_{file_counter}.xml")
            
            # Check if the file already exists, append the XML declaration only if it's a new file
            if current_size == 0 and not os.path.exists(output_file):
                with open(output_file, "wb") as out_f:
                    out_f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
                    out_f.write(b'<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/">\n')

    
    elif event == "end" and element.tag == "{http://www.mediawiki.org/xml/export-0.11/}page":
        # When we reach the end of a <page> element, process the page
        page_size = len(etree.tostring(element))

        # Check if adding this page exceeds the max size
        if current_size + page_size > MAX_SIZE:
            # If we exceed the size, close the current chunk and start a new one
            with open(output_file, "ab") as out_f:
                out_f.write(b"</mediawiki>\n")

            # Increment the file counter for the next file
            file_counter += 1

            # Reset the output file path with the updated counter
            output_file = os.path.join(output_dir, f"{namespace_subject}_{file_counter}.xml")
            
            # Start a new chunk file with the XML declaration and <mediawiki> tag
            with open(output_file, "wb") as out_f:
                out_f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
                out_f.write(b'<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/">\n')

            # Reset current size after starting a new file
            current_size = 0

        # Add the current page to the chunk
        with open(output_file, "ab") as out_f:
            out_f.write(etree.tostring(element, pretty_print=True))
        
        current_size += page_size

    # Clear the element to save memory
    element.clear()

# Close the last chunk with </mediawiki>
if output_file:
    with open(output_file, "ab") as out_f:
        out_f.write(b"</mediawiki>\n")

print(f"Splitting complete. Files saved in {output_dir}.")

spark.stop()


