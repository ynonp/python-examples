"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""

from random import randint

while True:
    cand = randint(1, 1000000)

    if cand % 7 != 0: continue
    if cand % 13 != 0: continue
    if cand % 15 != 0: continue

    print "Number is:", cand
    break

