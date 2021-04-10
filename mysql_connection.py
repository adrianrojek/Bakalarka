import mysql.connector


def open_connection():
  mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="bakalarka"
  )
  return mydb


mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="bakalarka"
)




