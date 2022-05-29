from lxml import etree, objectify
from io import BytesIO
from Klasser.Lessons import Lessons
from ToXML.Elements import Elements


class LessonToXML:
    def __init__(self, lessons: Lessons):
        self.lessons = lessons

    def write_file(self):

        root = etree.Element("les")
        for lesson in self.lessons.get_lessons():
            lesson_element = Elements.create_lesson(lesson)
            root.append(lesson_element)

        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        parser = etree.XMLParser(remove_blank_text=True)
        file_obj = BytesIO(etree.tostring(root))
        tree = etree.parse(file_obj, parser)

        try:
            with open("Lesson.xml", "wb") as xml_writer:
                tree.write(xml_writer, pretty_print=True, encoding='utf-8', xml_declaration=True)
        except IOError:
            pass

