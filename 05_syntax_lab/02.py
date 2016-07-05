"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""

from random import randint

total = 0

for _ in range(7):
    num = randint(1,100)
    total += num

print "Total sum is: %d" % total
if total % 7 == 0: print "Boom!"

