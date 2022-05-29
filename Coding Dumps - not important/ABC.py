from abc import ABC, abstractmethod

class DAO(ABC):
#class DAO(metaclass=abc.ABCMeta):
    """
    An interface class to database access and other persistent storage
    https://en.wikipedia.org/wiki/Data_access_object
    The syntax is a bit tricky, but necessary if your want to implement a
    so-called 'formal interface'. It uses Abstract Base Classes (abc) - full doc here
    https://docs.python.org/3.9/library/collections.abc.html
    For explanation see eg https://realpython.com/python-interface/
    This interface class states that the implementing classes should have three
    callable methods: setup(), connect(), close()
    """


@abstractmethod
def setup(self):
    pass


@abstractmethod
def connect(self):
    pass


@abstractmethod
def close(self):
    pass