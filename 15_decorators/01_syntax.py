"""
Decorators provide a generic way to pass code blocks to other
functions, mainly for implementing template algorithms.
"""
from functools import wraps

def print_in_matrix(f):
    @wraps(f)
    def wrapped(x,y):
        for i in range(x):
            for j in range(y):
                print f(i,j),
            print

    return wrapped


@print_in_matrix
def print_numbers_in_matrix(i, j):
    return "(%d,%d)" % (i,j)

@print_in_matrix
def print_mul_in_matrix(i,j):
    return "%d" % (i * j)

@print_in_matrix
def print_sum_in_matrix(i,j):
    return "%d" % (i + j)

print_numbers_in_matrix(5,5)
print_mul_in_matrix(5,5)
print_sum_in_matrix(5,5)


print sum.__name__
print print_mul_in_matrix.__name__












