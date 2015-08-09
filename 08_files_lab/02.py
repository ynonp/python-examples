"""
Write a program that takes 3 names. The first two
are existing file names and the last is a new file name
Program should write the lines from the first two 
files interwinded into the output file
"""

import itertools
import sys

if len(sys.argv) != 4:
    print "Usage: %s <file1> <file2> <file3>" % sys.argv[0]
    sys.exit(1)

(_,file1,file2,file_out) = sys.argv

with open(file1,"r") as fin1:
    with open(file2,"r") as fin2:
        with open(file_out,"w") as fout:
            for (l1,l2) in itertools.izip_longest(fin1, fin2, fillvalue=""):
                fout.write(l1 + l2)

