"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""

from random import randint

num = randint(1,9999)
print "Starting with: %d" % num

# Numeric calculation
num_i = num

sum_d = 0
while num_i != 0:
    digit = num_i % 10
    sum_d += digit
    num_i /= 10

print "Total sum of digits =", sum_d

# String calculation
num_s = str(num)
total = 0
for digit in num_s:
    total += int(digit)

print "Total = ",total
