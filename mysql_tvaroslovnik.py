import mysql.connector


def open_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="USER",
        password="PASSWORD",
        database="tvaroslovnik"
    )
    return mydb



