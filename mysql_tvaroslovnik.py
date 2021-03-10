import mysql.connector


def open_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kiklop10",
        database="tvaroslovnik"
    )
    return mydb



