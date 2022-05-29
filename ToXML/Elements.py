from lxml import objectify
from Klasser.Lessons import Lesson

class Elements:
    def create_lesson(lesson_obj: Lesson):
        lesson = objectify.Element("les")
        lesson.IDlesson = getattr(lesson_obj, "IDlesson")
        lesson.type = getattr(lesson_obj, "type")
        lesson.date = getattr(lesson_obj, "date")
        lesson.starttime = getattr(lesson_obj, "starttime")
        lesson.endtime = getattr(lesson_obj, "endtime")
        lesson.university = getattr(lesson_obj, "university")
        lesson.room = getattr(lesson_obj, "room")
        return lesson
