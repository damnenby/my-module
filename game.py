"""
game.py is the main execution file
"""

from settings import TEXT_TO_START
from exceptions import GameOver, EnemyDown

import models
import settings as sett


def play():
    print('Hey! You got into the world of the magic and battles!')
    print('Please, enter your name: ')
    player_name = input()
    enemy_level = 1
    player = models.Player(player_name)
    enemy = models.Enemy(1)
    print('Allowed attacks: ')
    for i in range(1, len(sett.ALLOWED_ATTACKS) + 1):
        print(f'{i} : {sett.ALLOWED_ATTACKS[i]}')

    print('To start the game print start below')
    if input('Here you go: ') == TEXT_TO_START:
        print('Lets fight')
        while True:
            try:
                player.attack(enemy)
                player.defence(enemy)
            except EnemyDown:
                player.score += 5
                enemy_level += 1
                enemy = models.Enemy(enemy_level)
                print('You killed an enemy!')
                print(f'Your lives: {player.lives}\nYour score: {player.score}')


if __name__ == '__main__':
    try:
        play()
    except GameOver as err:
        print('Game over :(')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye')
