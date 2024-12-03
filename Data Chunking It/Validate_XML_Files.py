from lxml import etree
import os

def validate_xml(file_path):
    try:
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(file_path, parser)
        root = tree.getroot()
        print(f"{file_path} is well-formed. Root element: {root.tag}")
    except etree.XMLSyntaxError as e:
        print(f"XML Syntax Error in {file_path}: {e}")

output_dir = '/home/jessica/Documents/xml_chunks'
for file_name in os.listdir(output_dir):
    if file_name.endswith('.xml'):
        file_path = os.path.join(output_dir, file_name)
        validate_xml(file_path)
