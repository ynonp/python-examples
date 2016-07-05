"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""

from random import randint

x = randint(1,10)
y = randint(1,10)

cand = max(x, y)

while cand % x != 0 or cand % y != 0:
    cand += 1

print "x=%d,y=%d,lcm=%d" % (x, y, cand)

