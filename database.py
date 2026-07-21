import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # ithe tujha mysql password tak
        database="payroll_db"
    )
