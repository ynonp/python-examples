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
        key = frozenset(word)
        words.setdefault(key, []).append(word)

        # Same as:
        # if words.has_key(key):
        #     words[key].append(word)
        # else:
        #     words[key] = [word]

for (key, val) in words.items():
    print val

