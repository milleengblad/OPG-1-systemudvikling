class Skema:
    """Dette er en class for skema"""
    def __init__(self, IDschedule, date, time, room, lecture, course):
        self.IDschedule = IDschedule
        self.date = date
        self.time = time
        self.room = room
        self.lecture = lecture
        self.course = course

    def get_IDschedule(self): return self.IDschedule
    def set_IDschedule(self, new_IDschedule): self.IDschedule = new_IDschedule

    def get_date(self): return self.date
    def set_date(self, new_date): self.date = new_date

    def get_time(self): return self.time
    def set_time(self, new_time): self.time = new_time

    def get_room(self): return self.room
    def set_room(self, new_room): self.room = new_room

    def get_lecture(self): return self.lecture
    def set_lecture(self, new_lecture): self.lecture = new_lecture

    def get_course(self): return self.course
    def set_course(self, new_course): self.course = new_course

