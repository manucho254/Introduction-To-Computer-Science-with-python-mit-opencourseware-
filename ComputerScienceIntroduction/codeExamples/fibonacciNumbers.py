# find fibonacci numbers efficient

def fib(x):
    """assume x an in >= 0
       returns Fibonacci of x
    """
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib(x-1) + fib(x-2)


print(fib(10))