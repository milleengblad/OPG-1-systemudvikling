from DummyOBJ import dummyObjects
from LessonToXML import LessonToXML
from XMLToLesson import XMLToLesson

if __name__ == "__main__":

    lessonList = dummyObjects.create()
    LessonToXML(lessonList).write_file()

    lessonList = XMLToLesson("Lesson.xml").parseXML()

    lessons = lessonList.get_lessons()

    for lesson in lessons:
        print("-" * 30)
        print()
        print("Lesson: ", getattr(lesson, "IDlesson"), getattr(lesson, "type"), getattr(lesson, "date"), getattr(lesson, "starttime"), getattr(lesson, "endtime"), getattr(lesson, "university"), getattr(lesson, "room"))