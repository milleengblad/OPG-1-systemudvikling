from Klasser.Lesson import Lesson

class Lessons:
    def __init__(self):
        self.lessons = []

    def append_lessons(self, lesson: Lesson):
        self.lessons.append(lesson)

    def get_lessons(self):
        return self.lessons
