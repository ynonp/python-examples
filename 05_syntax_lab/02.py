"""
Write a Python program that randomizes 7 numbers
and prints their sum total.
If the sum is divisable by 7, also print the word "Boom"
"""

from random import randint

total = 0

for _ in range(7):
    num = randint(1,100)
    total += num

print "Total sum is: %d" % total
if total % 7 == 0: print "Boom!"

