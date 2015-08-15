"""
Print only unique words from sys.argv
"""

import sys

s = set(sys.argv[1:])

print s

for i in s: print i,


