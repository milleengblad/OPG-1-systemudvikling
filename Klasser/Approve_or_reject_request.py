from enum import Enum
from datetime import date
from datetime import datetime

class type(Enum):
    SAU = 1
    Forelaesning = 2

class Approve_or_reject_request:
    """This is the class for the approval or rejection of deleting a course"""
    def __init__(self, IDrequest, IDlesson, type:type, date:date, time:datetime, location, room, request, approve, reject):
        self.IDrequest = IDrequest
        self.IDlesson = IDlesson
        self.type = type
        self.date = date
        self.time = time
        self.location = location
        self.room = room
        self.request = request
        self.approve = approve
        self.reject = reject

    def get_IDrequest(self): return self.IDrequest
    def set_IDrequest(self, new_IDrequest): self.IDrequest = new_IDrequest

    def get_IDlesson(self): return self.IDlesson
    def set_IDlesson(self, new_IDlesson): self.IDlesson = new_IDlesson

    def get_type(self): return self.type
    def set_type(self, new_type): self.type = new_type

    def get_date(self): return self.date
    def set_date(self, new_date): self.date = new_date

    def get_time(self): return self.time
    def set_time(self, new_time): self.time = new_time

    def get_location(self): return self.location
    def set_location(self, new_location): self.location = new_location

    def get_room(self): return self.room
    def set_room(self, new_room): self.room = new_room

    def get_request(self): return self.request
    def set_request(self, new_request): self.request = new_request

    def get_approve(self): return self.approve
    def set_approve(self, new_approve): self.approve = new_approve

    def get_reject(self): return self.reject
    def set_reject(self, new_reject): self.reject = new_reject
