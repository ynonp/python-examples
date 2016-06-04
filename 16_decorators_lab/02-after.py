"""Write a decorator called after5 that takes a
function and returns a new version of it that ignores
first 5 invocations"""

def after5(f):
    data = { 'counter' : 0 }
        
    def wrapper(*args, **kwargs):
        data['counter'] += 1
        if data['counter'] > 5: return f(*args, **kwargs)
        
    return wrapper

@after5
def doit(): print "Yo!"

# ignore the first 5 calls
doit()
doit()
doit()
doit()
doit()

# so only print yo once
doit()
