"""
1. Defining functions
2. Variadic functions
3. Keyword arguments
4. Lambda expressions
"""

def greet():
    print "***********"
    print "* Hello   *"
    print "***********"

def sum_digits(n):
    res = sum([int(d) for d in str(n)])
    return res

def my_sum(start,*args):
    res = start * start

    for n in args:
        res += n
    return res

def print_times(text="",times=5):
    for _ in range(times): print text

def count_score(text, **kwords):
    res = 0

    for word in text.split():
        res += kwords.get(word, 0)

    return res

print count_score("hit me baby one more time", me=10,you=20,they=17,more=5)







# greet()

# greet()

print sum_digits(235) + 5

print my_sum(2,5, 3)

print_times(text="Hello")
print_times(text="Hi There", times=2)






