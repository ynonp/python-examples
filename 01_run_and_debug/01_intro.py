""" Welcome To Python

A python program is just a text file.
We run python from command line with:
python program.py

We can also run the program in a built-in python
debugger with:
python -mpdb program.py
"""

# python ignores this one

print "Tell me your name"
name = raw_input()

for count in range(10):
    print "Welcome", name

