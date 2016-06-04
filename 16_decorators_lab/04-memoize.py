"""Write a decorator called memoize
that remembers past results of a function"""

def memoize(f):
    data = { }
        
    def wrapper(*args):
        if args not in data:
            data[args] = f(*args)
            
        return data[args]
        
    return wrapper        

@memoize
def fib(n):
    print "fib(%d)" % n
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print fib(100)