""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments

Bonus: Use argparse module to parse command line arguments
"""

import os
import argparse

parser = argparse.ArgumentParser(description='Deletes large files')

parser.add_argument('--path', help='path to search')
parser.add_argument('--threshold', help='minimum file size to delete')

args = parser.parse_args()

threshold = int(args.threshold) if args.threshold else 1024
path = args.path if args.path else "."

print "Searching for files > %d in %s" % (threshold, path)


for root, dirs, files in os.walk(path):
    for name in files:
        size = os.stat(name).st_size
        if size > threshold:
            print "Found: %s > %d" % (name, threshold)
            print "Do you want to delete it? (y/N)"
            yesno = raw_input()
            if yesno.lower() == "y": os.remove(name)

