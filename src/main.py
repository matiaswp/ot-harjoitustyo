import repositories.highscore_repository as highscore_repository
import sqlite3
from database_connection import get_database_connection

def main():
    connection = sqlite3.connect("data/database.sql")
    highscore_repo = highscore_repository.HighscoreRepository(connection)
    highscore_repo.add_score_to_highscores("nimi", 450)
    print(highscore_repo.get_one())
    

if __name__ == '__main__':
    main()


