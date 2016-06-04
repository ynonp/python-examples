"""Write a decorator called after5 that takes a
function and returns a new version of it that ignores
first 5 invocations"""

# With python3 our naive solution works
# so we don't need the dictionary.
def after5(f):
    n = 0
        
    def wrapper(*args, **kwargs):
# nonlocal is a new keyword in python3
# which tells python that from now on
# n refers to the one defined in an outer scope
        nonlocal n
        n += 1
        if n > 5: return f(*args, **kwargs)
        
    return wrapper

@after5
def doit(): print("Yo!")

# ignore the first 5 calls
doit()
doit()
doit()
doit()
doit()

# so only print yo once
doit()
