"""
Write a program that reads 10 numbers from
the user and prints the largest one
"""

max_number = int(raw_input())

for _ in range(9):
    num = int(raw_input())
    if num > max_number:
        max_number = num

print "Max number = %d" % max_number

