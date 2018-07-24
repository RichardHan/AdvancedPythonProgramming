
# Function
def my_hello_function():
    """ Function Documentation Sample"""
    print("Hello from a function")

# Function Arguments
def add_fun(x, y):
    return x + y
print (add_fun(20,5))

def shout(phrase="Yo!!"):
    print (phrase)

shout()
shout("YoYo!!!")

def fun_display_myname(fname):
    """  Display input unction Documentation"""
    print("My name is " + fname)

fun_display_myname("Richard")
fun_display_myname("RJ")

def write_log(message, prefix='DefaultPrefix'):
    """  Positional  + Keyword """
    print ('[%s] %s' % (prefix , message))

write_log('Application start', 'Main Function')
write_log('Login  start', 'Login Function')
write_log('Debug Information')

# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 ...
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)

for x in range(10):
    print 'x=' + str(x) + ' fib=' + str(fib(int(x)))
