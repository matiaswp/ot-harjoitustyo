import repositories.highscore_repository as highscore_repository
import sqlite3
from database_connection import get_database_connection

def main():
    connection = sqlite3.connect("data/database.sql")
    highscore_repo = highscore_repository.HighscoreRepository(connection)
    highscore_repo.add_score_to_highscores("testi", 250)
    top20 = highscore_repo.get_top20_highscores()
    print("Top score: " + str(top20[0][1]))
    

if __name__ == '__main__':
    main()


