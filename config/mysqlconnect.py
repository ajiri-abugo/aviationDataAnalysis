import mysql.connector

# connect to database
connection = mysql.connector.connect(user='ajiri', password='Avidjester32@43',host='localhost',database='travelagency')

# create cursor

cursor = connection.cursor()

cursor.execute(SQL)


cursor.execute(SQL)
connection.commit()


# query data


# close connection
connection.close()