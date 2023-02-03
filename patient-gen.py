from yattag import Doc,indent
import random

# generate a random string
def getName():
    random_string = '' 
    for _ in range(10):
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        random_string += (chr(random_integer))
    return random_string
 

# take either Kolkata or Delhi for now
def getCity():
    cities = ["Kolkata","Delhi"]
    return cities[random.randint(0,len(cities)-1)]

def getAge():
    return random.randint(10,80)


rec_num = int(input("Enter the number of records : "))
doc,tag,text = Doc().tagtext()

with tag('Patients'):
    for i in range(1,rec_num+1):
        with tag('patient'):
                with tag('id'):
                    text("{i}".format(i=i))
                with tag('name'):
                    text(getName())
                with tag('city'):
                    text(getCity())
                with tag('age'):
                    text(getAge())
                

result = indent(
    doc.getvalue(),
    indentation = ' '*4,
    newline =  '\r\n'
)


file = open("./xml_files/patient.xml","w")
file.writelines(result)
file.close()