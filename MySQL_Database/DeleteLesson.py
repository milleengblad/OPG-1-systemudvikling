import mysql.connector
#https://www.w3schools.com/sql/sql_select.asp - brut til kode

BestBooking_database = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='1234Bobkomodo',
    port='3306',
    database= 'BestBooking_database'
)

mycursor = BestBooking_database.cursor()

sql= "DELETE FROM Lektioner WHERE idLektioner ='4'"
mycursor.execute(sql)
BestBooking_database.commit()
print(mycursor.rowcount,"record(s) deleted")

'''
mycursor = BestBooking_database.cursor()
mycursor.execute('SELECT * FROM Lektioner')
Lektioner = mycursor.fetchall()

for user in Lektioner:
    print(user)

deletelesson = "DELETE FROM Lektioner WHERE idLektioner = '4'"

try:
    mycursor.execute(deletelesson, '4')
    print("Data deleted successfully")

except:
    print("Unable to delete the data")
BestBooking_database.commit()

BestBooking_database.close()
'''