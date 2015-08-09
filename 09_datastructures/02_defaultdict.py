"""
A default dictionary
"""

from collections import defaultdict

size = defaultdict(int)
# size = defaultdict(str)
# size = defaultdict(float)

size["foo"] = 10
size["bar"] = 20

print size["foo"]
print size["buz"]

