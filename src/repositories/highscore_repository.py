from database_connection import get_database_connection
import sqlite3

class HighscoreRepository:
    def __init__(self, connection):
        self.connection = sqlite3.connect("data/database.sql")

    def get_one(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "select name, score from highscores order by score DESC limit 1"
        )
        row = cursor.fetchone()
        return row
        

    def add_score_to_highscores(self, name, score):
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into highscores (name, score) VALUES (?,?)", (name,score)
        )
