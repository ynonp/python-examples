"""
The function reduce takes a list
and a function and reduces all items
using the function.

For example reduce [1,2,3,4] with a + yields 10
"""

s = reduce(
        lambda acc,val: acc + val,
        [1,2,3,4])

longest = reduce(
        lambda acc,val: acc if len(acc) > len(val) else val,
        "baby let me follow you down".split())

print s
print longest

