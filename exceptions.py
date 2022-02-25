"""
exceptions.py contains such exceptions as GameOver and EnemyDown
"""


class GameOver(Exception):
    """
    Class GameOver saves score and settings.py
    """

    def __init__(self, player_name, player_score):
        self.player_name = player_name
        self.player_score = player_score
        self.save_score()

    def save_score(self):
        """
        saves the score to scores.txt
        """
        with open('scores.txt', 'a', encoding="utf8") as scores_file:
            scores_file.write(f'{self.player_name} ended the game with {self.player_score} score\n')


class EnemyDown(Exception):
    pass
