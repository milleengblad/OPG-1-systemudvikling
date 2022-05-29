from enum import Enum
from datetime import date
from datetime import datetime

class type(Enum):
    SAU = 1
    Forelaesning = 2

class Lesson:
    """Class for lesson"""
    def __init__(self, IDlesson, type: type, date:date, starttime:datetime, endtime:datetime, university, room):
        self.IDlesson = IDlesson
        self.type = type
        self.date = date
        self.starttime = starttime
        self.endtime = endtime
        self.university = university
        self.room = room

    def get_IDlesson(self): return self.IDlesson
    def set_IDlesson(self, new_IDlesson): self.IDlesson = new_IDlesson

    def get_type(self): return self.type
    def set_type(self, new_type): self.type = new_type

    def get_date(self): return self.date
    def set_date(self, new_date): self.date = new_date

    def get_starttime(self): return self.starttime
    def set_starttime(self, new_starttime): self.starttime = new_starttime

    def get_endtime(self): return self.endtime
    def set_endtime(self, new_endtime): self.endtime = new_endtime

    def get_university(self): return self.university
    def set_university(self, new_university): self.university = new_university

    def get_room(self): return self.room
    def set_room(self, new_room): self.room = new_room