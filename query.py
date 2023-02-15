import argparse
import random
import time
import xml.etree.ElementTree as ET


def search_by_name(file:str, name:str, flag:str):
    if flag == "d":
        tree = ET.parse("data/doctor_"+file)
        root = tree.getroot()
        for doc in root.findall('doctor'):
            if doc.find("dName").text == name:
                return [doc.find("docId").text, doc.find("dName").text, doc.find("city").text, doc.find("age").text, doc.find("specialization").text]
    elif flag == "p":
        tree = ET.parse("data/patient_"+file)
        root = tree.getroot()
        for doc in root.findall('patient'):
            if doc.find("ptName").text == name:
                return [doc.find("ptId").text, doc.find("ptName").text, doc.find("city").text, doc.find("age").text]


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--doctorname')
parser.add_argument('-p', '--patientname')

args = parser.parse_args()

files = ["age_0.xml","age_1.xml","city_0.xml","city_1.xml"]

if args.doctorname:
    hit = 1
    start = time.time()
    x = random.randint(0,3)
    print("Searching in ",files[x])
    rec = search_by_name(files[x], args.doctorname, "d")
    if rec == None:
        if(x==0):
            print("Searching in ",files[1])
            rec = search_by_name(files[1], args.doctorname, "d")
        elif(x==1):
            print("Searching in ",files[0])
            rec = search_by_name(files[0], args.doctorname, "d")
        elif(x==2):
            print("Searching in ",files[3])
            rec = search_by_name(files[3], args.doctorname, "d")
        else:
            print("Searching in ",files[2])
            rec = search_by_name(files[2], args.doctorname, "d")
        hit = 2
    print(rec)
    print("total time taken  ",(time.time()-start)*1000)

if args.patientname:
    hit = 1
    start = time.time()
    x = random.randint(0,3)
    print("Searching in ",files[x])
    rec = search_by_name(files[x], args.patientname, "p")
    if rec == None:
        if(x==0):
            print("Searching in ",files[1])
            rec = search_by_name(files[1], args.patientname, "p")
        elif(x==1):
            print("Searching in ",files[0])
            rec = search_by_name(files[0], args.patientname, "p")
        elif(x==2):
            print("Searching in ",files[3])
            rec = search_by_name(files[3], args.patientname, "p")
        else:
            print("Searching in ",files[2])
            rec = search_by_name(files[2], args.patientname, "p")
        hit = 2
    print(rec)
    print("total time taken  ",(time.time()-start)*1000)