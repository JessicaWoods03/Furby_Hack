# handling xml parsing from wiki dump
# https://dumps.wikimedia.org/enwiki/20240701/
# file = enwiki-20240701-pages-meta-history1.xml-p1p812.bz2 2.4 GB
# file = enwiki-20240701-pages-meta-history1.xml-p813p1460.bz2 2.0 GB

import xml.etree.ElementTree as ET
from lxml import etree

# make this furby a double smarter than just one dump file
xml_dump_file = '/home/jessica/PycharmProjects/Furby_Hack/enwiki-20240701-pages-meta-history1.xml-p1p812-'
tree = ET.parse(xml_dump_file)
# xml_dump_file2 = 'enwiki-20240701-pages-meta-history1.xml'
# empty root
root = tree.getroot()
# this was to look at the scheme inorder to do the element tree
with open(xml_dump_file, 'r', encoding='utf-8') as file:
    for i in range(10):
        print(i)
        print(file.readline().strip())


# Define the namespace
namespace = {'mediawiki': 'http://www.mediawiki.org/xml/export-0.11/'}

# Iterate through each <page> element
context = etree.iterparse(xml_dump_file, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.11/}page')

for event, elem in context:
    # Process each <page> element here
    title = elem.find('mediawiki:title', namespaces=namespace).text
    revisions = elem.findall('mediawiki:revision', namespaces=namespace)

    print(f"Title: {title}")
    print(f"Number of revisions: {len(revisions)}")
    print("-" * 20)

    # Clear the element to free memory
    elem.clear()

    # Also clear the parent element to release memory
    while elem.getprevious() is not None:
        del elem.getparent()[0]

# Clear the entire context to free up memory
del context
