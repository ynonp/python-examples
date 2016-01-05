""" Main project file
"""
import lib.board as board

from lib.player import Player
from lib.board import Game

def print_board(game):
    for i in range(board.ROWS):
        for j in range(board.COLS):
            print "%2s" % game.val(i,j),
        print

if __name__ == "__main__":
    p1 = Player("Bob", "X")
    p2 = Player("Jane", "O")

    g = Game()

    g.start(p1, p2)

    while True:
        move = raw_input()
        try:
            (row,col) = [int(n) for n in move.split()]
            g.play(row,col)

            print_board(g)

            if g.winner is not None:
                print "Game Over, %s won" % g.winner.name
                break

            if g.tie():
                print "Game Over, it's a tie"
                break

        except ValueError as e:
            print "Expected move format: row col"

        except board.GameException as e:
            print e, ". Try again"

