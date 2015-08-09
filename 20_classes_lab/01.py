"""
The following code assumes a class
named Summer exists. 
Complete the class so correct result is printed
"""

class Summer(object):
    def __init__(self):
        self._total = 0

    def add(self, *vals):
        self._total += sum(vals)

    def total(self):
        return self._total

s = Summer()
t = Summer()

s.add(10,20)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()
