"""
Write a python program that takes two words
as sys.argv and prints only the letters
common to both
"""

import sys

(_, w1, w2) = sys.argv

print set(w1).intersection(set(w2))

print [l for l in w1 for g in w2 if l == g]

