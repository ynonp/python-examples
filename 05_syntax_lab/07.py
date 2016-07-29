""" Write a program that selects a random number
and asks the user to guess it.

After each guess print a hint "too large" or "too small" to the user.

Bonus: To make things interesting, the program should cheat once in a white
"""

from random import randint

secret = randint(1,100)

while 1:
    print "Guess a number:"
    guess = int(raw_input())
    if guess == secret:
        print "You Win"
        break
    
    cheating = randint(1,7) % 7 == 0
    if not cheating:
        if guess < secret:
            print "Too Small"
        else:
            print "Too Large"
    else:
# Cheating!
        if guess < secret:
            print "Too Large"
        else:
            print "Too Small"


