"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""
from functools import reduce

def mysum(*args):
    return sum([n for n in args if type(n) == int])

def mymul(*args):
    return reduce(
            lambda a,b: a * b,
            [n for n in args if type(n) == int])

print(mysum(10, 20, 30, 'foo', 'bar', 40))
print(mymul(1, 2, 3, 'foo', 'bar', 4))

