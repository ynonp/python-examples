""" While Break demo"""

while True:
    print "Please type in a number"
    num = int(raw_input())

    if num % 2 == 0:
        print "Bravo, it's an even number"
    else:
        break

print "The End"


