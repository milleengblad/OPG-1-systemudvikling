from lxml import objectify
from Klasser.Lesson import Lesson
from Klasser.Lessons import Lessons

class XMLToLesson:
    def __init__(self, xml_filename):
        self.xml_filename = xml_filename

    def parseXML(self) -> Lessons:
        with open(self.xml_filename, "rb") as f:
            xml = f.read()

        root = objectify.fromstring(xml)

     #   attributes = root.attrib

        lessonList = Lessons()

        for lesson in root.getchildren():
            lesson_obj = Lesson(lesson.IDlesson, lesson.type, lesson.date, lesson.starttime, lesson.endtime, lesson.university, lesson.room)

            lessonList.append_lessons(lesson_obj)
        return lessonList