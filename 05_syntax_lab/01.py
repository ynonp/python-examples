"""
Write a program that reads 10 numbers from
the user and prints the largest one
"""

max_number = int(input())

for _ in range(9):
    num = int(input())
    if num > max_number:
        max_number = num

print("Max number = %d" % max_number)

