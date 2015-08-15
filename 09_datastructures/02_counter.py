"""
Count how many letters in a word
and print them sorted, using a Counter
"""

from collections import Counter

print "Please type in a word"
word = raw_input()

freq = Counter(word)

print freq

for k in sorted(freq, key=freq.get, reverse=True):
    print "%s => %d" % (k, freq[k])

