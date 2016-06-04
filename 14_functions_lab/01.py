"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""

def numeric_reduce(op, *args):
    return reduce(
            op,
            [n for n in args if type(n) == int])

def mysum(*args):
    return numeric_reduce(lambda a,b: a+b, *args)

def mymul(*args):
    return numeric_reduce(lambda a,b: a*b, *args)


print mysum(10, 20, 30, 'foo', 'bar', 40)
print mymul(1, 2, 3, 'foo', 'bar', 4)

