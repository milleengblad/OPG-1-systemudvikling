from Klasser.Lesson import Lesson
from Klasser.Lessons import Lessons

class dummyObjects:
    @staticmethod
    def create():
        lessonList = Lessons()
        lesson1 = Lesson(1, "Forelæsning", 20220329, 10, "KU", 105, 11)
        lesson2 = Lesson(2, "Forelæsning", 20220329, 11, "KU", 105, 12)
        lessonList.append_lessons(lesson1)
        lessonList.append_lessons(lesson2)
        return lessonList