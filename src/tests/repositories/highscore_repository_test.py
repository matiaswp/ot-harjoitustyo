import unittest
from repositories.highscore_repository import highscore_repo

class TestHighscoreRepository(unittest.TestCase):
    def setUp(self):
        highscore_repo.delete_all()

    def test_get_top_20_highscores_first_highest(self):
        name1 = "Liisa"
        name2 = "Matti"
        name3 = "Kalevi"
        name4 = "Miika"
        score1 = 280
        score2 = 329
        score3 = 230
        score4 = 335
        highscore_repo.add_score_to_highscores(name1, score1)
        highscore_repo.add_score_to_highscores(name2, score2)
        highscore_repo.add_score_to_highscores(name3, score3)
        highscore_repo.add_score_to_highscores(name4, score4)
        top20 = highscore_repo.get_top20_highscores()
        self.assertEqual(top20[0][1], score4)

    def test_get_top_20_highscores_last_lowest(self):
        name1 = "Liisa"
        name2 = "Matti"
        name3 = "Kalevi"
        name4 = "Miika"
        score1 = 280
        score2 = 329
        score3 = 230
        score4 = 335
        highscore_repo.add_score_to_highscores(name1, score1)
        highscore_repo.add_score_to_highscores(name2, score2)
        highscore_repo.add_score_to_highscores(name3, score3)
        highscore_repo.add_score_to_highscores(name4, score4)
        top20 = highscore_repo.get_top20_highscores()
        self.assertEqual(top20[3][1], score3)