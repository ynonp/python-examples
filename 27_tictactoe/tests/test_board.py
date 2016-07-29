import lib.board as board
from lib.player import Player

import unittest

class TestGameplay(unittest.TestCase):
    def setUp(self):
        self.g = board.Game()
        self.p1 = Player("bob", "X")
        self.p2 = Player("Jane", "O")

        self.g.start(self.p1, self.p2)

    def test_switchplayers(self):
        self.g.play(0,0)
        self.assertEqual(self.g.current_player, self.p2)

    def test_illegalmove(self):
        self.g.play(0,0)
        with self.assertRaises(board.InvalidMove):
            self.g.play(0,0)

    def test_false_tie(self):
        # board is empty, no tie
        self.assertFalse(self.g.tie())

    def test_true_tie(self):
        self.g.play(0,0)
        self.g.play(0,1)
        self.g.play(0,2)
        self.g.play(1,1)
        self.g.play(1,0)
        self.g.play(1,2)
        self.g.play(2,1)
        self.g.play(2,0)
        self.g.play(2,2)
        self.assertTrue(self.g.tie())


class TestWin(unittest.TestCase):
    def setUp(self):
        self.g = board.Game()
        self.p = Player('demo', 'X')
        self.g.current_player = self.p
        
    def test_winning_row(self):
        p = self.p
        self.g.data = [
            [None, None, None],
            [p, p, p],
            [None, None, None],
        ]
        self.g.checkwinner()
        self.assertEqual(self.g.winner, self.p)

    def test_winning_col(self):
        p = self.p
        self.g.data = [
            [p, None, None],
            [p, None, None],
            [p, None, None],
        ]
        self.g.checkwinner()
        self.assertEqual(self.g.winner, self.p)

    def test_winning_diag(self):
        p = self.p
        self.g.data = [
            [p, None, None],
            [None, p, None],
            [None, None, p],
        ]
        self.g.checkwinner()
        self.assertEqual(self.g.winner, self.p)


