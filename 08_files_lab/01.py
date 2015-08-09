"""
Write a program that takes 2 file names
and appends the second file's contents to
the end of the first one
"""

import sys

if len(sys.argv) != 3:
    print "Usage: %s <file1> <file2>" % sys.argv[0]
    sys.exit(1)

(_, file1,file2) = sys.argv

with open(file1,"r") as fin:
    with open(file2,"a") as fout:
        for line in fin:
            fout.write(line)

