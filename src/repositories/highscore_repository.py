from database_connection import get_database_connection
import sqlite3

class HighscoreRepository:
    def __init__(self, connection):
        self.connection = connection

    def get_top20_highscores(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "select name, score from highscores order by score DESC limit 20"
        )
        top20 = cursor.fetchall()
        return top20
        

    def add_score_to_highscores(self, name, score):
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into highscores (name, score) VALUES (?,?)", (name,score)
        )
        self.connection.commit()

    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE * FROM highscores")
        self.connection.commit()

highscore_repo = HighscoreRepository(sqlite3.connect("data/database.sql"))