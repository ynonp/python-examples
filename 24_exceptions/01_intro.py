"""
Exceptions in python
1. Catching exceptions
2. Raising exceptions
3. Built-in exception types
4. User defined exceptions
"""

def foo():
    bar()
    print "hello"

def bar():
    print "bar start"
    res = 1/0
    print "bye bye"



print "welcome master"
foo()

print "the end"

