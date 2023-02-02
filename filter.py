import xml.etree.ElementTree as ET
import shutil
import sys

## AGE
# say we want all patients with age > 40 in another xml file
# 1. remove patients <= 40 from that file
# 2. for mutual exclusiveness remove > 40 from original file as well

tree = ET.parse('patient.xml')
root = tree.getroot()

for patient in root.findall('patient'):
    age = int(patient.find('age').text)
    if age <= 40:
        root.remove(patient)

tree.write('patientGT40.xml')

tree = ET.parse('patient.xml')
root = tree.getroot()

for patient in root.findall('patient'):
    age = int(patient.find('age').text)
    if age > 40:
        root.remove(patient)
tree.write('patientLT40.xml')

## CITY
tree = ET.parse('patient.xml')
root = tree.getroot()

for patient in root.findall('patient'):
    city = patient.find('city').text
    if city == 'Delhi':
        root.remove(patient)

tree.write('patientKol.xml')


tree = ET.parse('patient.xml')
root = tree.getroot()

for patient in root.findall('patient'):
    city = patient.find('city').text
    if city == 'Kolkata':
        root.remove(patient)

tree.write('patientDel.xml')