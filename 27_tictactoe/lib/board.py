ROWS = 3
COLS = 3

from itertools import cycle
import re

class GameException(Exception):pass
class InvalidMove(GameException):pass
class GameOver(GameException):pass

BLANK = '.'

WINNERS = [
    r'([^.])..\1..\1..',
    r'.([^.])..\1..\1.',
    r'..([^.])..\1..\1',
    r'([^.])\1\1......',
    r'...([^.])\1\1...',
    r'......([^.])\1\1',
    r'([^.])...\1...\1',
    r'..([^.]).\1.\1..',
]

class Game(object):
    def __str__(self):
        # Game as string is used to check
        # for winners and for debug purposes
        return ''.join([self.val(row,col) 
                for row in range(ROWS) 
                for col in range(COLS)])

    def __init__(self):        
        self.clearboard()
        self.winner = None

            
    def val(self, row, col):
        p = self.data[row][col]
        if p is None:
            return BLANK
        else:
            return p.val

    def start(self,p1, p2):
        # cycle will return an object that
        # each call to its next() method will
        # return the next cycled item from the array
        self.players = cycle([p1, p2])

        self.current_player = self.players.next()
        self.clearboard()

    def clearboard(self):
        # The game board is a double array
        # in which each item is the player currently
        # taking this square, or None if the square is empty
        self.data = []
        for i in range(ROWS):
            row = []
            for j in range(COLS):
                row.append(None)
            self.data.append(row)


    def play(self,row,col):
        # Check move is within range
        if row > ROWS or row < 0 or col > COLS or col < 0: 
            raise InvalidMove("(%d,%d) out of range" %(row,col))

        # Check game is not over
        if self.winner is not None: raise GameOver()

        # Check square is free
        p = self.data[row][col]
        if p is not None: raise InvalidMove("(%d,%d) is already taken" % (row,col))
        
        # Set value in square and check for a winning move
        self.data[row][col] = self.current_player
        self.checkwinner()

        # Set next player for the next round
        self.current_player = self.players.next()

    def checkwinner(self):
        # The list of winning moves is saved
        # in the array WINNERS as a list of regular
        # expressions.
        # If any of them matches, we have a winner
        for state in WINNERS:
            match = re.search(state, str(self))
            if match is not None:
                self.winner = self.current_player
                

    def tie(self):
        return BLANK not in str(self) and self.winner is None

