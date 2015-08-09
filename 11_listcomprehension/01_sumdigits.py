"""
Using List Comprehensions

1. Caluclate sum of digits
2. A list of squares
3. Count comment lines
4. Combining lists
5. Reduce function
"""

n = 12345
str(n)
"12345"

print sum([int(x) for x in str(n)])

numbers = range(100)
print sum(numbers)
print sum([x * x for x in numbers])

