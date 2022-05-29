from abc import abstractmethod
from MySQL_Database.ABC import ABC
from Klasser.Lesson import Lesson
from typing import List  # needed to be able to declare list type

from MySQL_Database.LessonSearchType import LessonSearchType


class LessonABC(ABC):

    @abstractmethod
    def insert_lesson(self, les: Lesson):
        pass

    @abstractmethod
    def update_lesson(self, les: Lesson) -> bool:
        pass

    @abstractmethod
    def delete_lesson(self, les: Lesson) -> bool:
        pass

    @abstractmethod
    def find_lesson_by_property(self, search_type: LessonSearchType, value: object) -> List[Lesson]:
        pass

    @abstractmethod
    def find_all(self) -> List[Lesson]:
        pass