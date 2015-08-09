"""
Raising custom exceptions
"""

class InvalidMove(Exception): pass

def foo(x):
    raise ValueError("%d is not good" % x)

def bar(x):
    raise InvalidMove("error invalid move")

bar(10)

