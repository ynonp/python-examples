"""
Catching and handling exceptions demo
"""

import sys

while True:
    line = sys.stdin.readline()
    if line == "": break

    try:
        (x, y) = [int(n) for n in line.split()]
        print "%d + %d = %d" % (x, y, x + y)
        print "%d / %d = %d" % (x, y, x / y)

    except ValueError as e:
        print "You must type only numbers"

    except ZeroDivisionError as e:
        print "Sorry, can't divide by zero"




