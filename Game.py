from objects import Board
from objects import Hero
from objects import Monster


class Game(object):
    def __init__(self):
        self.board = Board.Board(5)
        self.hero = Hero.Hero(1, 1, '*')
        self.monster = Monster.Monster(3, 3, '@')
        self.lst = list()
        self.lst.append(self.hero)
        self.lst.append(self.monster)

    def update(self):
        for item in self.lst:
           item.update()

    def print(self):
        self.board.start_print()
        for item in self.lst:
            self.board.print(item)
        print (self.board.board)

if __name__ == '__main__':
    game = Game()
    game.update()
    game.print()