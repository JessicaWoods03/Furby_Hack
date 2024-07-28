# still ran into memory issues chunking this down so resorted to streaming options
#so this should stream it so its going to hopefully work

from lxml import etree
import os

def split_xml(input_file, output_dir, chunk_size):
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

    # Use the namespace for parsing
    ns = {'mw': 'http://www.mediawiki.org/xml/export-0.11/'}

    context = etree.iterparse(input_file, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.11/}page')
    file_count = 0
    current_chunk = []
    
    print(f"Starting to split {input_file} into chunks...")

    try:
        for event, elem in context:
            # Convert the current <page> element to a string and add it to the chunk
            current_chunk.append(etree.tostring(elem, pretty_print=True, encoding='unicode'))

            # Clear the element to free up memory
            elem.clear() 

            # If we reach the chunk size, write to a new file
            if len(current_chunk) >= chunk_size:
                chunk_file_path = os.path.join(output_dir, f'chunk_{file_count}.xml')
                with open(chunk_file_path, 'w', encoding='utf-8') as f:
                    f.write('<pages>\n')  # Root element for the chunk
                    f.write('\n'.join(current_chunk))
                    f.write('\n</pages>')
                print(f"Created {chunk_file_path} with {len(current_chunk)} pages.")
                file_count += 1
                current_chunk = []  # Reset for the next chunk

        # Write any remaining pages to a new file
        if current_chunk:
            chunk_file_path = os.path.join(output_dir, f'chunk_{file_count}.xml')
            with open(chunk_file_path, 'w', encoding='utf-8') as f:
                f.write('<pages>\n')
                f.write('\n'.join(current_chunk))
                f.write('\n</pages>')
            print(f"Created {chunk_file_path} with {len(current_chunk)} pages.")

    except Exception as e:
        print(f"An error occurred: {e}")

    print(f"Finished processing. Created {file_count + 1} chunk files.")

# Usage
input_file = '/home/jessica/Documents/enwiki-20240701-pages-meta-history1.xml'
output_dir = '/home/jessica/Documents/xml_chunks'
chunk_size = 100  # Adjust chunk size to lower if necessary

split_xml(input_file, output_dir, chunk_size)

