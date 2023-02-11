import xml.etree.ElementTree as ET
import random

class Helper:
    def __init__(self, num_nodes:int, doc_rec:int, pt_rec:int, trt_rec:int, vs_rec:int) -> None:
        self.num_nodes = num_nodes
        self.doc_records = doc_rec
        self.pt_records = pt_rec
        self.tr_records = trt_rec
        self.vs_records = vs_rec

    def generate_doctor_data(self):
        roots = {}
        for i in range(self.num_nodes):
            root1 = ET.Element("root")
            root2 = ET.Element("root")
            roots[f"root_city_{i}"]=  root1
            roots[f"root_age_{i}"] = root2

        for i in range(1,self.doc_records+1):
            city = self._getCity()
            age = self._getAge()
            name = self._getName()
            spec = self._getSpecialization()

            if city == "Kolkata":
                doc = ET.Element("doctor")
                roots[f"root_city_0"].append(doc)
                ET.SubElement(doc, "docId", name="doctor Id").text = str(i)
                ET.SubElement(doc, "dName", name="doctor Name").text = name
                ET.SubElement(doc, "city", name="doctor city").text = city
                ET.SubElement(doc, "specialization", name="doctor spec").text = spec
                ET.SubElement(doc, "age", name="doctor age").text = str(age)
            else:
                doc = ET.Element("doctor")
                roots[f"root_city_1"].append(doc)
                ET.SubElement(doc, "docId", name="doctor Id").text = str(i)
                ET.SubElement(doc, "dName", name="doctor Name").text = name
                ET.SubElement(doc, "city", name="doctor city").text = city
                ET.SubElement(doc, "specialization", name="doctor spec").text = spec
                ET.SubElement(doc, "age", name="doctor age").text = str(age)

            if age < 50:
                doc = ET.Element("doctor")
                roots[f"root_age_0"].append(doc)
                ET.SubElement(doc, "docId", name="doctor Id").text = str(i)
                ET.SubElement(doc, "dName", name="doctor Name").text = name
                ET.SubElement(doc, "city", name="doctor city").text = city
                ET.SubElement(doc, "specialization", name="doctor spec").text = spec
                ET.SubElement(doc, "age", name="doctor age").text = str(age)
            else:
                doc = ET.Element("doctor")
                roots[f"root_age_1"].append(doc)
                ET.SubElement(doc, "docId", name="doctor Id").text = str(i)
                ET.SubElement(doc, "dName", name="doctor Name").text = name
                ET.SubElement(doc, "city", name="doctor city").text = city
                ET.SubElement(doc, "specialization", name="doctor spec").text = spec
                ET.SubElement(doc, "age", name="doctor age").text = str(age)

        for i in range(self.num_nodes):
            tree = ET.ElementTree(roots[f"root_city_{i}"])
            tree.write(f"data/doctor_city_{i}.xml")
            tree = ET.ElementTree(roots[f"root_age_{i}"])
            tree.write(f"data/doctor_age_{i}.xml")

    def generate_patient_data(self):
        roots = {}
        for i in range(self.num_nodes):
            root1 = ET.Element("root")
            root2 = ET.Element("root")
            roots[f"root_city_{i}"]=  root1
            roots[f"root_age_{i}"] = root2

        for i in range(1,self.pt_records+1):
            city = self._getCity()
            age = self._getAge()
            name = self._getName()

            if city == "Kolkata":
                doc = ET.Element("patient")
                roots[f"root_city_0"].append(doc)
                ET.SubElement(doc, "ptId", name="id").text = str(i)
                ET.SubElement(doc, "ptName", name="name").text = name
                ET.SubElement(doc, "city", name="city").text = city
                ET.SubElement(doc, "age", name="age").text = str(age)
            else:
                doc = ET.Element("patient")
                roots[f"root_city_1"].append(doc)
                ET.SubElement(doc, "ptId", name="id").text = str(i)
                ET.SubElement(doc, "ptName", name="name").text = name
                ET.SubElement(doc, "city", name="city").text = city
                ET.SubElement(doc, "age", name="age").text = str(age)

            if age < 50:
                doc = ET.Element("patient")
                roots[f"root_age_0"].append(doc)
                ET.SubElement(doc, "ptId", name="id").text = str(i)
                ET.SubElement(doc, "ptName", name="name").text = name
                ET.SubElement(doc, "city", name="city").text = city
                ET.SubElement(doc, "age", name="age").text = str(age)
            else:
                doc = ET.Element("patient")
                roots[f"root_age_1"].append(doc)
                ET.SubElement(doc, "ptId", name="id").text = str(i)
                ET.SubElement(doc, "ptName", name="name").text = name
                ET.SubElement(doc, "city", name="city").text = city
                ET.SubElement(doc, "age", name="age").text = str(age)

        for i in range(self.num_nodes):
            tree = ET.ElementTree(roots[f"root_city_{i}"])
            tree.write(f"data/patient_city_{i}.xml")
            tree = ET.ElementTree(roots[f"root_age_{i}"])
            tree.write(f"data/patient_age_{i}.xml")

    def generate_treatment_data(self):
        pass

    def generate_visit_data(self):
        pass

    def _getName(self):
        random_string = '' 
        for _ in range(10):
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            random_string += (chr(random_integer))
        return random_string
 
    def _getCity(self):
        cities = ["Kolkata","Delhi"]
        return cities[random.randint(0,len(cities)-1)]

    def _getSpecialization(self):
        spls = ["Cardiology","Neurology","ENT","Eye","Nephrology","Nutrition","Orthopedics"]
        return spls[random.randint(0,len(spls)-1)]

    def _getAge(self):
        return random.randint(20,80)