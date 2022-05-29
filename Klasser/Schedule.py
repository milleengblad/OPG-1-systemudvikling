from datetime import datetime
from datetime import date

class Skema:
    """Class for schedule"""
    def __init__(self, IDschedule, date:date, starttime: datetime, endtime: datetime, room, lecture, course):
        self.IDschedule = IDschedule
        self.date = date
        self.starttime = starttime
        self.endtime = endtime
        self.room = room
        self.lecture = lecture
        self.course = course

    def get_IDschedule(self): return self.IDschedule
    def set_IDschedule(self, new_IDschedule): self.IDschedule = new_IDschedule

    def get_date(self): return self.date
    def set_date(self, new_date): self.date = new_date

    def get_starttime(self): return self.starttime
    def set_starttime(self, new_starttime): self.starttime = new_starttime

    def get_endtime(self): return self.endtime
    def set_endtime(self, new_endtime): self.endtime = new_endtime

    def get_room(self): return self.room
    def set_room(self, new_room): self.room = new_room

    def get_lecture(self): return self.lecture
    def set_lecture(self, new_lecture): self.lecture = new_lecture

    def get_course(self): return self.course
    def set_course(self, new_course): self.course = new_course

