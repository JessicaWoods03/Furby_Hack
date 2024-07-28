from lxml import etree
import os

def split_xml(input_file, output_dir, chunk_size):
    os.makedirs(output_dir, exist_ok=True)
    context = etree.iterparse(input_file, events=('end',), tag='page')
    file_count = 0
    current_chunk = []

    for event, elem in context:
        current_chunk.append(etree.tostring(elem, pretty_print=True, encoding='unicode'))
        elem.clear()  # Clear the element to free memory

        # If we reach the chunk size, write to a new file
        if len(current_chunk) >= chunk_size:
            with open(os.path.join(output_dir, f'chunk_{file_count}.xml'), 'w', encoding='utf-8') as f:
                f.write('<pages>\n')  # Root element for the chunk
                f.write('\n'.join(current_chunk))
                f.write('\n</pages>')
            file_count += 1
            current_chunk = []  # Reset for the next chunk

    # Write any remaining pages to a new file
    if current_chunk:
        with open(os.path.join(output_dir, f'chunk_{file_count}.xml'), 'w', encoding='utf-8') as f:
            f.write('<pages>\n')
            f.write('\n'.join(current_chunk))
            f.write('\n</pages>')

# Usage
split_xml('/home/jessica/Documents/enwiki-20240701-pages-meta-history1.xml', 
           '/home/jessica/Documents/xml_chunks', chunk_size=1000)
