"""
Write a function toCamelCase(text) that returns the text camel cased
Write a function to_underscore(text) that returns the text with 
underscores between words
"""

import re

def toCamelCase(text):
    return re.sub(r'_([a-z])',
            lambda m: m.group(1).upper(),
            text)

def to_underscore(text):
    return re.sub(r'([a-z])([A-Z])',
            lambda m: m.group(1) + "_" + m.group(2).lower(),
            text)


print toCamelCase('welcome')
print toCamelCase('hello_world')
print toCamelCase('get_name')
print toCamelCase('no_more_shall_we_part')

print to_underscore('welcome')
print to_underscore('helloWorld')
print to_underscore('getName')
print to_underscore('noMoreShallWePart')
