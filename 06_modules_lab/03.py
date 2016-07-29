""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""

import os
import sys

threshold = 1024
path = "."

if len(sys.argv) > 1:
    path = sys.argv[1]

if len(sys.argv) > 2:
    threshold = int(sys.argv[2])


for root, dirs, files in os.walk(path):
    for name in files:
        size = os.stat(name).st_size
        if size > threshold:
            print "Found: %s > %d" % (name, threshold)
            print "Do you want to delete it? (y/N)"
            yesno = raw_input()
            if yesno.lower() == "y": os.remove(name)
