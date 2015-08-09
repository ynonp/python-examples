"""
Write a function that takes minlen and
a list of words, and returns only the words
longer than minlen
"""

def longer_than(minlen, *args):
    return [word for word in args if len(word) > minlen]


print longer_than(4, "foo", "bar", "fantastic", "python", "abc")

