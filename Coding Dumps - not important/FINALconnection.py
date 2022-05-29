import mysql.connector
#https://www.w3schools.com/sql/sql_select.asp - brut til kode

class Mysql_connector:
    """hjjhj"""
    BestBooking_database = None
    mycursor = None

    def __init__(self):
        self.BestBooking_database = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='1234Bobkomodo',
            port='3306',
            database='BestBooking_database')
        self.mycursor = self.BestBooking_database.cursor()

      #  self.mycursor.execute('SELECT * FROM Lektioner')
       # self.Lektioner = self.mycursor.fetchall()

#for user in Lektioner:
#    print(user)


def all_lessons(self):
    deletelesson = ("DELETE FROM Lektioner WHERE idLektioner = '4'")
    try:
        self.mycursor.execute(deletelesson)
       # print("Data deleted successfully")
        result = self.mycursor.fetchall()


    except:

        print("Unable to delete the data")

    return result

#BestBooking_database.close()

db = Mysql.connector()
print(db.all_lessons())



