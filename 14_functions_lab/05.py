"""
Write a function groupby that takes a list
and a function and returns a dictionary
keyd by the return value of the function on the list items

For example:
    groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])
    returns: { 'f': ['foo','fi'], 'h': ['hello', 'hi'] }
"""

def groupby(f, words):
    res = {}
    for word in words:
        key = f(word)
        res.setdefault(key, []).append(word)

    return res

print groupby(lambda s: frozenset(s), ['add', 'dad', 'help','rome', 'more'])
