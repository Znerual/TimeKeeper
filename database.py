import sqlite3 as sq3

class Database:
    def __init__(self):
        connection = sq3.connect("chronik.db")
        cursor = connection.cursor
        cursor.execute("""CREATE TABLE IF NOT EXISTS chronik (startTime INTEGER, endTime INTEGER, comment TEXT, title TEXT);""")
        cursor.commit()
        connection.close()
