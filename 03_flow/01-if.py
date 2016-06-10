""" Control Flow:
        If
        While
        For  
"""           

print "Please type in a number"
number = int(raw_input())

if number % 2 == 0:
    print "Even"
elif number % 3 == 0:
    print "Divides in 3"    
else:
    print "Odd"