from MySQL_Database.LessonABC import LessonABC
from Klasser.Lesson import Lesson
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import pooling
from MySQL_Database.LessonSearchType import LessonSearchType
from typing import List # needed to be able to declare list type

class MySQLLessonABC(LessonABC):
    DBB = 'BestBooking_database'

    __pool__: pooling.MySQLConnectionPool
    __cnx__: mysql.connector.connection = None
    cursor = None

    @classmethod
    def create_database(cls):

        cls.__cnx__ = mysql.connector.connect(user = 'root', password = '1234Bobkomodo', host = '127.0.0.1')

        cursor = cls.__cnx__.cursor()
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(cls.DBB))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    @classmethod
    def setup(cls):
        cls.__cnx__ = mysql.connector.connect(user = 'root', password = '1234Bobkomodo', host = '127.0.0.1')

        cursor = cls.__cnx__.cursor()
        try:
            cursor.execute("USE {}".format(cls.DBB))
        except mysql.connector.Error as err:
            print("Database {} does not exists".format(cls.DBB))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                cls.create_database()
                print("Database {} created succesfully".format(cls.DBB))
                cls.__cnx__.databse = cls.DBB
            else:
                print(err)
                exit(1)

        create = """ look in mysql DML script - Lessons """
        with cls.__cnx__.cursor() as cursor:
            cursor.execute(create)
    @classmethod
    def connect(cls):
        try:
            cls.__pool__ = pooling.MySQLConnectionPool(pool_name="minpool", pool_size=7, user='root', password='1234Bobkomodo', host='127.0.0.1', database=cls.DBB)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("UPS! noget er galt med dit username eller password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Databasen eksisterer ikke")
            else:
                print(err)

        cls.__cnx__ = cls.__pool__.get_connection()
        print("connection", cls.__cnx__)

    def close(cls):
        if cls.__cnx__ is not None:
            cls.__cnx__.close()

    @classmethod
    def insert_lesson(cls, les: Lesson):
        IDlesson = les.get_IDlesson()
        type = les.get_type()
        date = les.get_date()
        starttime = les.get_starttime()
        endtime = les.get_endtime()
        university = les.get_university()
        room = les.get_room()

        insert = """BestBooking_database.Lesson (IDlesson, type, date, starttime, endtime, university, room)""".format(IDlesson, type, date, starttime, endtime, university, room)

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(insert)
            cls.__cnx__.commit()

    @classmethod
    def update_lesson(cls, les: Lesson):
        IDlesson = les.get_IDlesson()
        type = les.get_type()
        date = les.get_date()
        starttime = les.get_starttime()
        endtime = les.get_endtime()
        university = les.get_university()
        room = les.get_room()

        update = """BestBooking_database.Lesson (IDlesson, type, date, starttime, endtime, university, room)""".format(IDlesson, type, date, starttime, endtime, university, room)

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(update)
            cls.__cnx__.commit()

    @classmethod
    def delete_lesson(cls, les: Lesson):
        IDlesson = les.get_IDlesson()

        delete = """Delete from BestBooking_database.Lesson where IDlesson =""" .format(IDlesson)

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(delete)
            cls.__cnx__.commit()

    def find_Lesson_by_property(self, search_type: LessonSearchType, value: object) -> List[Lesson]:
        pass

    @classmethod
    def find_all(cls) -> List[Lesson]:

        query = "SELECT * FROM BestBooking_database.Lesson"
        print("findall connection", cls.__cnx__)
        cursor = cls.__cnx__.cursor(dictionary=True)
        # with cls.__cnx__.cursor(dictionary = True) as cursor:
        cursor.execute(query)
        all_lessons = cursor.fetchall()
        print(all_lessons)
        print(cls.__pool__)
        return all_lessons
