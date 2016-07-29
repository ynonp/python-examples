""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""

import sys

(program_name, num1, num2) = sys.argv

print "%g + %g = %g" % (float(num1), float(num2), float(num1) + float(num2))
