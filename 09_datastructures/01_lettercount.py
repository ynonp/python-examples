"""
Count how many letters in a word
and print them sorted
"""

print "Please type in a word"
word = raw_input()

freq = {}

for letter in word:
    count = freq.setdefault(letter, 0)
    freq[letter] = count + 1


print freq

for k in sorted(freq, key=freq.get, reverse=True):
    print "%s => %d" % (k, freq[k])

