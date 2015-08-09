"""
Write a function that takes two arguments: 
    A string
    And a number
If wrong types were passed in, raise an exception
"""

def take_string_and_number(s,n):
    if type(s) != str: raise ValueError("First Argument should be string")
    if type(n) != int: raise ValueError("Second should be int")


take_string_and_number('hello', 10)
take_string_and_number('hello', 'world')


