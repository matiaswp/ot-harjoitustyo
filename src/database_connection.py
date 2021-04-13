import os
import sqlite3
dirname = os.path.dirname("data/database.sql")

connection = sqlite3.connect("data/database.sql")
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection