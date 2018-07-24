
# Function
def my_hello_function():
    """ Function Documentation Here"""
    print("Hello from a function")

# Function Arguments
def add_fun(x, y):
    return x + y
print add_fun(20,5)
"""
25
"""

def shout(phrase="Yo!!"):
    print (phrase)

shout()
shout("YoYo!!!")
"""
Yo!!
YoYo!!!
"""

def write_log(message, prefix='DefaultPrefix'):
    """  Positional  + Keyword """
    print ('[%s] %s' % (prefix , message))

write_log('Application start', 'Main Function')
write_log('Login  start', 'Login Function')
write_log('Debug Information')
"""
[Main Function] Application start
[Login Function] Login  start
[DefaultPrefix] Debug Information
"""

# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 ...

def recursion_fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return recursion_fib(n-1)+recursion_fib(n-2)

print recursion_fib(10)
"""
55
"""
for i in range(10):
    print 'i=' + str(i) + ' fib=' + str(recursion_fib(int(i)))
"""
x=0 fib=0
x=1 fib=1
x=2 fib=1
x=3 fib=2
x=4 fib=3
x=5 fib=5
x=6 fib=8
x=7 fib=13
x=8 fib=21
x=9 fib=34
"""