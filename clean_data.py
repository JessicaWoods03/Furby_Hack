import xml.etree.ElementTree as ET

def extract_and_clean_large_xml(xml_file, output_file):
    context = ET.iterparse(xml_file, events=("end",))
    # Initialize a buffer to accumulate text
    buffer = []
    namespaces = {'mw': 'http://www.mediawiki.org/xml/export-0.11/'}
    
    with open(output_file, 'w') as out_file:
        for event, elem in context:
            if elem.tag.endswith('text'):  # Check if tag is 'text' in your namespace
                text = elem.text
                if text:
                    cleaned_text = text.replace('\n', ' ').strip()
                    buffer.append(cleaned_text)
                    
                    # Write to file periodically to avoid high memory usage
                    if len(buffer) > 1000:  # Adjust batch size as needed
                        out_file.write('\n'.join(buffer) + '\n')
                        buffer = []
            elem.clear()  # Clear the element to free up memory

        # Write any remaining buffer content
        if buffer:
            out_file.write('\n'.join(buffer) + '\n')

# Example usage, for memory sake I did it one at a time instead of looping threw each file
# in the xml chunks folder
extract_and_clean_large_xml('/home/jessica/Documents/xml_chunks/chunk_4.xml', '/home/jessica/Documents/cleaned_chunk_4.txt')
