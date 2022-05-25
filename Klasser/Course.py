class Kursus:
    """Dette er en class for kursus"""
    def __init__(self, IDcourse, course_name, duration, location, university):
        self.IDcourse = IDcourse
        self.course_name = course_name
        self.duration = duration
        self.location = location
        self.university = university

    def get_IDcourse(self): return self.IDcourse
    def set_IDcourse(self, new_IDcourse): self.IDcourse = new_IDcourse

    def get_course_name(self): return self.course_name
    def set_course_name(self, new_course_name): self.course_name = new_course_name

    def get_duration(self): return self.duration
    def set_duration(self, new_duration): self.duration = new_duration

    def get_location(self): return self.location
    def set_location(self, new_location): self.location = new_location

    def get_university(self): return self.university
    def set_university(self, new_university): self.university = new_university