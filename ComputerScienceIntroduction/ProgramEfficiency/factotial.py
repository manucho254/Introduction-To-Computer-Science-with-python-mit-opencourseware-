""" 
    Iterative factorial O(n)
"""

def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
        
    return prod

print(fact_iter(6))


""" 
    recursive factorial O(n) Linear recursion
"""

def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n*fact_recur(n-1)

print(fact_iter(6))


