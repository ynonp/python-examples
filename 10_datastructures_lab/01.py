"""
Write a program that takes two strings
from the user and checks if they represent
a valid user name.
Valid users and passwords:
    apple => red
    lettuce => green
    lemon => yellow
    orange => orange
"""

pwd = {
    'apple'   : 'red',
    'lettuce' : 'green',
    'lemon'   : 'yellow',
    'orange'  : 'orange',
}

print "Please type in your name"
name = raw_input()

print "What's the password?"
password = raw_input()

if pwd.has_key(name) and pwd[name] == password:
    print "Welcome, Master"
else:
    print "INTRUDER ALERT"


















