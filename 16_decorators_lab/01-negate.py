"""Write a decorator that negates its function
Causing boolean functions that return True to
return False and vice versa"""

from functools import wraps

def negate(f):
    @wraps(f)
    def wrapper(*args):
        return not f(*args)
        
    return wrapper

@negate
def yo(x,y):
    print x    
    return True

print yo(x=10,y=20)
