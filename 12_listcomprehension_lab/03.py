"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

import string

print [a + b + c 
        for a in string.lowercase
        for b in string.lowercase
        for c in string.lowercase]

