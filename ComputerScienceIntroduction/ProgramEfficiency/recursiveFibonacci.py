""" 
  Recursive Fibonacci  complexity O(2n)
"""

def fib_recur(n):
    """ assumes n an in >= 0 """
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)
    
print(fib_recur(10))