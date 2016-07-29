""" Write a program that takes a count
from sys.argv import and prints "Hello Python"
count times
"""
import sys

count = int(sys.argv[1])

for i in range(count):
    print "Hello Python"
