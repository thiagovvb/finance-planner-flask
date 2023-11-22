import sqlite3
import os

class Database():

    def __init__(self):
        if not os.path.isfile('./db.sqlite'):
            self.database = sqlite3.connect('db.sqlite')
            self.run_creates()

    def run_creates(self):

        cur = self.database.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                [user_id] INTEGER PRIMARY KEY, 
                [email] VARCHAR(100),
                [password] VARCHAR(100)
            )""")

    def get_database(self):
        return self.database

    
