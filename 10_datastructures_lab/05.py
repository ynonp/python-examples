"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""

import sys
(_,fname) = sys.argv

words = {}

with open(fname, 'r') as f:
    for line in f:
        word = line.rstrip()
        key = tuple(sorted(word))

        words.setdefault(key, []).append(word)

print words.values()

