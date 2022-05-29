import mysql.connector
from mysql.connector import errorcode


class MySQL_Database:
    """Klasse for connector"""
    my_database = None
    MY_courser = None

    def __init__(self):
        self.my_database = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='1234Bobkomodo',
            database='BestBooking_database'
        )
        self.my_courser = self.my_database.cursor()

    def all_Lesson(self, mode='DESC'):
        sql_lesson = (SELECT * idLektioner FROM Lesson WHERE idLektioner = '4')
        try:
            self.my_courser.execute(sql_lesson)
            result = self.my_courser.fetchall()
        except Exception as error:
            return error

        return result

    def check_error(self):
        try:
            my_database = mysql.connector.connect(user='root', database='BestBooking_database')

        except mysql.connector.connect.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Ups! Der skete en fejl - noget gald med brugernavn eller kodeord")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Valgte database eksisterer ikke")
            else:
                print(e)

        else:
            my_database.close()

DBB = MySQL_connector()
print(DBB.all_Lessons())

