# still ran into memory issues chunking this down so resorted to streaming options
#so this should stream it so its going to hopefully work
#still had to adjust with swap files to do this program because it still blew up LOL
# changed swap file to 16GB which is unique option for linux

from lxml import etree
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def split_xml(input_file, output_dir, chunk_size=100):
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    context = etree.iterparse(input_file, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.11/}page')
    chunk = []
    count = 0
    file_index = 0  # Index for naming chunk files

    for event, elem in context:
        chunk.append(etree.tostring(elem).decode())
        count += 1

        if count >= chunk_size:
            # Save the chunk to a new file
            with open(os.path.join(output_dir, f'chunk_{file_index}.xml'), 'w') as f:
                f.write("<mediawiki>\n" + "\n".join(chunk) + "\n</mediawiki>")
            logger.info(f"Saved chunk_{file_index}.xml with {count} pages.")
            file_index += 1  # Increment file index for the next chunk
            chunk = []
            count = 0

        # Clear the element to save memory
        elem.clear()

    # Save any remaining pages
    if chunk:
        with open(os.path.join(output_dir, f'chunk_{file_index}.xml'), 'w') as f:
            f.write("<mediawiki>\n" + "\n".join(chunk) + "\n</mediawiki>")
        logger.info(f"Saved chunk_{file_index}.xml with {len(chunk)} pages.")

# Usage
input_file = '/home/jessica/Documents/enwiki-20240701-pages-meta-history1.xml'
output_dir = '/home/jessica/Documents/xml_chunks'
chunk_size = 100  # Adjust chunk size to lower if necessary

# Split the XML file
split_xml(input_file, output_dir, chunk_size)


