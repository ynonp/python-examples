"""
Write a python program that takes numbers in a loop
and for each number prints its square root
If value is negative or not a number show 
a warning and keep reading values
"""

import sys
import math

while True:
    line = sys.stdin.readline().rstrip()
    if line == "": break

    try:
        val = float(line)
        sqrt = math.sqrt(val)

    except ValueError as e:
        print "Sorry try again"

    else:
        print "sqrt(%f) = %f" % (val, sqrt)




