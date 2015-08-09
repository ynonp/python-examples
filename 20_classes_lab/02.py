"""
Following code assumes a class named MyCounter
Fill in the code so correct result is printed
"""
class MyCounter(object):
    count = 0

    def __init__(self):
        MyCounter.count += 1

for _ in range(10):
    c1 = MyCounter()

# should print 10
print MyCounter.count
