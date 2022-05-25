class Lesson:
    """Dette er en class for sekretær"""
    def __init__(self, IDlesson, type, date, time, location, room):
        self.IDlesson = IDlesson
        self.type = type
        self.date = date
        self.time = time
        self.location = location
        self.room = room

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