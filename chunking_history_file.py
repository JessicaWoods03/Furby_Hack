# I had to pull a history from my desktop GitHub, to show some of the original code
# I used to do the first bit of chunking. That resulted in 5 Chunks. I started chasing a few 
# bugs and lost track of the original code that was the first start of chunking.

import os

def split_xml(input_file, output_dir, chunk_size):
    os.makedirs(output_dir, exist_ok=True)
    context = etree.iterparse(input_file, events=('end',), tag='page')
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

    # Use the namespace for parsing
    ns = {'mw': 'http://www.mediawiki.org/xml/export-0.11/'}

    context = etree.iterparse(input_file, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.11/}page')
    file_count = 0
    current_chunk = []
    page_count = 0  # Counter for pages

    # Debugging message for starting the split
    print(f"Starting to split {input_file} into chunks...")

    for event, elem in context:
        current_chunk.append(etree.tostring(elem, pretty_print=True, encoding='unicode'))
        elem.clear()  # Clear the element to free memory
    try:
        for event, elem in context:
            current_chunk.append(etree.tostring(elem, pretty_print=True, encoding='unicode'))
            elem.clear()  # Clear the element to free memory
            page_count += 1  # Increment page count

        # If we reach the chunk size, write to a new file
        if len(current_chunk) >= chunk_size:
            with open(os.path.join(output_dir, f'chunk_{file_count}.xml'), 'w', encoding='utf-8') as f:
                f.write('<pages>\n')  # Root element for the chunk
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
            file_count += 1
            current_chunk = []  # Reset for the next chunk
            print(f"Created {chunk_file_path} with {len(current_chunk)} pages.")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Write any remaining pages to a new file
    if current_chunk:
        with open(os.path.join(output_dir, f'chunk_{file_count}.xml'), 'w', encoding='utf-8') as f:
            f.write('<pages>\n')
            f.write('\n'.join(current_chunk))
            f.write('\n</pages>')
    print(f"Total <page> elements processed: {page_count}")

# Usage
split_xml('/home/jessica/Documents/enwiki-20240701-pages-meta-history1.xml', 
           '/home/jessica/Documents/xml_chunks', chunk_size=1000)
input_file = '/home/jessica/Documents/enwiki-20240701-pages-meta-history1.xml'
output_dir = '/home/jessica/Documents/xml_chunks'
chunk_size = 1000  # Adjust chunk size as needed

split_xml(input_file, output_dir, chunk_size)
