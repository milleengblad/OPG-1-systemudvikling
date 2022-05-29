import xml.etree.ElementTree as xml

def GenerateXML(fileName):
    root=xml.Element("Lessons")
    c1=xml.Element("lesson")
    root.append(c1)
    IDlesson1=xml.SubElement(c1, "IDlesson")
    IDlesson1.text="1"

    type1=xml.SubElement(c1, "type")
    type1.text="Forelæsning"

    date1=xml.SubElement(c1, "date")
    date1.text="2022-03-09"

    starttime1=xml.SubElement(c1, "starttime")
    starttime1.text="10:15:00"

    endtime1=xml.SubElement(c1, "endtime")
    endtime1.text="11:00:00"

    university1=xml.SubElement(c1, "university")
    university1.text="KU"

    room1=xml.SubElement(c1, "room")
    room1.text="105"

    tree=xml.ElementTree(root)
    with open(fileName, "wb") as files:
        tree.write(files)

if __name__=="__main__":
    GenerateXML("XMLGenerated.xml")
