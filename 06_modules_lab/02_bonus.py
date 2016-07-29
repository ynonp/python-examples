""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
Bonus: Print error messages for invalid inputs.

To print error messages we'll have to use a concept not yet learned in the
course, and which will only be presented later: Exceptions.
We'll tap into python's error handling and change its default
error message to something more meaningful.
"""

import sys

try:
    (program_name, num1, num2) = sys.argv
    print "%g + %g = %g" % (float(num1), float(num2), float(num1) + float(num2))
except ValueError as e:
    print "Error - Usage %s <num1> <num2>" % sys.argv[0]
except Exception as e:
    print "Something went wrong: ", e

