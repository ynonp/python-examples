"""
Write a program that reads data
from property files.
Each line in the file can either be:
    An empty line
    A comment line (Start with #)
    A property line (of the form key = value)

Write a program that takes a property file name and key
as command line arguments and prints the requested value
"""

import sys
import re

props = sys.argv[1]
keys  = sys.argv[2:]
data  = {}

with open(props, 'r') as f:
    for line in f:
        m = re.search(r'(\w+)\s*=\s*(\w+)', line)
        if m is not None:
            k = m.group(1)
            val = m.group(2)
            data[k] = val

print "Debug", data
print "---"

for name in keys:
    print data[name]

