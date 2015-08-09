"""
Write a program that prints only unique values
from sys.argv (without program name)
"""

import sys

s = set()

print s.union(sys.argv[1:])

