"""
  Functions python
"""

def is_even(i: int) -> int:
    """
        Input: i is a positive int
        Returns True if i is even , otherwise False
    """
    
    print("inside is_even")
    
    return i % 2 == 0

print(is_even(5))

def f(x: int) -> int:
    x = x + 1
    print('in f(x): x =', x)
    return x

x = 3
z = f(x)

def is_even_with_return(i):
    """
        Input: i is a positive int
        Returns True if i is even , otherwise False
    """
    
    print("with return")
    remainder = i % 2
    
    return remainder == 0

is_even_with_return(3) # <- False
print(is_even_with_return(3))


def is_even_without_return(i):
    """
        Input: i is a positive int
        Returns None since no return statement is provided
    """
    
    print("without return")
    remainder = i % 2

is_even_without_return(3) # <- None
print(is_even_without_return(3))


#re using is_even funtion
print("All numbers between 0 and 20: even or not")
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")
        
        
#nested function

def g(x) :
    def h():
        x = "abc"
    x = x + 1
    print('g: x =', x)
    h()
    return x

x = 3
z = g(x)