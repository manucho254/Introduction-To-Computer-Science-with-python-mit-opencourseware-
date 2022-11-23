""" 
    Understanding program efficiency
"""

import time

def c_to_f(c):
    return c*9/5 + 32

t0 = time.time()
c_to_f(100000)
t1 = time.time() - t0
print("t = ", t0, ":", t1, "s,")


""" Counting Operations
"""

def c_to_f(c):
    return c*9.0/5 + 32

print(c_to_f(10))

def my_sum(x):
    total = 0
    for i in range(x+1):
        total += 1
    return total

print(my_sum(10000))


""" Simple search algorithm """

def search_for_element(L, e):
    for i in L:
        if i == e:
            return True
    return False   
    