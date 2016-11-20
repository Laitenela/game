from random import choice
from objects import Hero


class Monster(object):

    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def update(self):
        wasd = choice(['W','A','S','D'])
        if wasd.upper() == 'W':
            self.y -= 1
        elif wasd.upper() == 'A':
            self.x += 1
        elif wasd.upper() == 'S':
            self.y += 1
        elif wasd.upper() == 'D':
            self.x -= 1