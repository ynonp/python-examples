"""
1. Stringify: __str__ 
2. Override equality: __eq__, __ne__, __hash__
3. Other special methods
"""

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point (%d,%d)" % (self.x, self.y)

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.x) & hash(self.y)

    def __eq__(self, other):
        if type(other) == Point:
            return (self.x == other.x and self.y == other.y)
        else:
            return NotImplemented

p = Point(10,10)
q = Point(10,10)

if p != q:
    print "Wow p == q"
else:
    print "Oh no..."

if p is q:
    print "p and q are the same object"


