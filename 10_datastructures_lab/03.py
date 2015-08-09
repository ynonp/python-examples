"""
Define a list of 20 grades
and print only the grades that
are above average
"""

grades = [99, 90, 15, 28, 38, 44, 50, 81, 79, 60, 99, 90, 15, 28, 38, 44, 50,
        81, 79, 60 ]

avg = float(sum(grades)) / len(grades)

print "Average is: %d" % avg

for g in grades:
    if g > avg: print g



