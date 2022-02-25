"""
models.py contains such classes as Enemy, Player
"""


from random import randint
from exceptions import EnemyDown
from exceptions import GameOver
from settings import START_LIVES
from settings import ALLOWED_ATTACKS


class Enemy:

    """
    Class Enemy
    Attributes: level, lives
    Methods: static select_attack, decrease_lives
    """

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()


class Player:
    """
    Class Player
    Attributes: name, score, lives, allowed_attacks'
    Methods: static fight, decrease_lives, attack, defence
    """
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = START_LIVES
        self.allowed_attacks = ALLOWED_ATTACKS

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self.name, self.score)

    @staticmethod
    def fight(att, defence):
        if att == 1 and defence == 2 or att == 2 and defence == 3 or att == 3 and defence == 1:
            return 1
        if att == 1 and defence == 3 or att == 3 and defence == 2 or att == 2 and defence == 1:
            return -1
        if att == 1 and defence == 1 or att == 2 and defence == 2 or att == 3 and defence == 3:
            return 0

    def attack(self, enemy_obj):
        choice = int(input('Choose how to attack: '))

        fight_result = Player.fight(choice, Enemy.select_attack())

        if fight_result == 0:
            print('It is a draw!')
        if fight_result == 1:
            enemy_obj.decrease_lives()
            print('You attacked successfully')
        if fight_result == -1:
            self.decrease_lives()
            print('You missed!')

    def defence(self, enemy_obj):
        choice = int(input('Choose how to attack: '))

        fight_result = Player.fight(Enemy.select_attack(), choice)

        if fight_result == 0:
            print('It is a draw!')
        if fight_result == 1:
            enemy_obj.decrease_lives()
            print('You missed!')
        if fight_result == -1:
            self.decrease_lives()
            print('You attacked successfully!')
