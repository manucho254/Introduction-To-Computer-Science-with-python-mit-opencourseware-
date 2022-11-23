"""
  Recursion and Dictionaries
"""

def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(mult_iter(2, 100))


def mult_iter(a, b):
    if b == 1:
        return a
    return a + mult_iter(a, b-1)

print(mult_iter(2, 100))

# find factorial of a number

# Recusive solution
def fact(n):
    if n == 1:
        return 1
 
    return n * fact(n-1)

print(fact(4))

# iterative solution

def factorial_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
        
    return prod


# move items from tower recursively

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
    
def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
        
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
  
Towers(1, 2, 3, 4)      
        
#dictionaries

my_dict = {}
grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A'}

grades['John'] # evaluates to "A+"
# grades['cool'] # gives a KeyError

#add item to dictionary

grades['John'] = "A"

# check if key in dictionary

'John' in grades # returns True
'Daniel' in grades # returns False

# check if key and value in dictionary

del(grades['John'])

#get all keys in a dictionary

grades.keys() # ['Ana', 'Denise'] 

#get all values in a dictionary

grades.values() # ['B', 'A'] 

#get all items in a dictionary

grades.items() # {'Ana': 'B', 'Denise': 'A'}






    
    