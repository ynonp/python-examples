"""Write a decorator called debug that prints
its functions inputs and outputs"""

def debug(f):
    def wrapper(*args, **kwargs):
        print "[] Debug: args=%s; kwargs=%s" % (args, kwargs)
        res = f(*args, **kwargs)
        print "[] Done: %s" % res
        return res
        
    return wrapper


def sum_digits(n):
    digits = str(n)
    result = 0

    for char in digits:
        result += int(char)

    return result

print sum_digits(1531221)

