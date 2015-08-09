import sys

unique_words = set()
total_words = 0

for line in sys.stdin:
    words = line.split()
    total_words += len(words)
    unique_words = unique_words.union(words)

print "Unique / Total = %f" % (float(len(unique_words)) / total_words)
print "Unique words: ", unique_words
