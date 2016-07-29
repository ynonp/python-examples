"""
Write a program that randomizes a number
and prints the sum total of its digits.
For example if the number was: 2345
The result should be: 14
"""

from random import randint

num = randint(1,10000)
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
