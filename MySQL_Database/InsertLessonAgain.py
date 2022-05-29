'''
import mysql.connector
from datetime import date, datetime
#https://www.w3schools.com/sql/sql_select.asp - brut til kode

BestBooking_database = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='1234Bobkomodo',
    port='3306',
    database='BestBooking_database'
)
#add_lesson = ("INSERT INTO Lektioner""(idLektioner, Type, Starttid, Room_nr, idKurser, idUniversitet, idAnsatte, Sluttid)" "VALUES(4, 'SAU', 2022-04-01 09:15:00, 210, 1, 1, 102, 2022-04-01 10:00:00)")

mycursor = BestBooking_database.cursor()
sql = "INSERT INTO Lektioner (idLektioner, Type, Starttid, Room_nr, idKurser, idUniversitet, idAnsatte, Sluttid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
val = ("4", "SAU", "2022-04-01 09:15:00", "210", "1", "1", "102", "2022-04-01 10:00:00")
mycursor.execute(sql, val)
BestBooking_database.commit()

print(mycursor.rowcount, "record inserted.")
'''
#mycursor.execute("INSERT INTO Lektioner(idLektioner, Type, Starttid, Room_nr, idKurser, idUniversitet, idAnsatte, Sluttid) VALUES(4, 'SAU', 2022-04-01 09:15:00, 210, 1, 1, 102, 2022-04-01 10:00:00);")
#print(" Data Inserted!!!")

#BestBooking_database.commit()
#BestBooking_database.close()
