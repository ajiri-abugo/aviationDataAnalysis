import mysql.connector

#database connection
conn = None
try:
    conn = mysql.connector.connect(
        host = "localhost",
        user = "ajiri",
        password = "Avidjester32@43",
        port = "3306",
        database = "travelagency")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    print("error connecting to staging database")
else:
    print("connected to staging database")
finally:
    if conn:
        conn.close()