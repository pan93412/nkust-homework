import json

import xmltodict

import xml.etree.ElementTree as ET

tree = ET.parse('05-xml-example.xml')
root = tree.getroot()

# find lecturer
print(root.find("*/participants/lecturer").text)
print(len(root.findall("*/participants/student")))
print(root.find("*/participants/student[1]").text)
print(root.find("*/participants/student[1]").get('grade'))