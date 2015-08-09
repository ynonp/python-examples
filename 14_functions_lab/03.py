"""
Write a function that calculates the sum
of the 10th digit from all arguments passed to it
"""


def sum_tens(*args):
    return sum([(n / 10) % 10 for n in args])


print sum_tens(120, 140, 1123)
