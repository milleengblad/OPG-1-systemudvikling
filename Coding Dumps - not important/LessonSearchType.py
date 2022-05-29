from enum import unique, Enum


@unique
class LessonSearchType(Enum):
    """
    Class for enumerating lessons
    """

    IDlesson = 1
    type = 2
    date = 3
    starttime = 4
    endtime = 5
    university = 6
    room = 7
