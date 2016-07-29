"""
Write a program that takes 3 names. The first two
are existing file names and the last is a new file name/
The program should write the lines from the first two 
files interwinded into the output file. So if we have

a.txt with
a1
a2

and b.txt with
b1
b2

then running

python 02.py a.txt b.txt c.txt
will result in the creation of c.txt with the following content:

a1
b1
a2
b2

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

