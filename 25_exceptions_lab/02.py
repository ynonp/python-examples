"""
Write a program that takes a file name
and prints line count for the file

Alert the user politely if there was any problem opening the file
"""

import sys

(_, filename) = sys.argv

count = 0
try:
    with open(filename, 'r') as f:
        for line in f:
            count += 1

except IOError as e:
    print "Failed to open file.", e

else:
    print "File had %d lines" % count

