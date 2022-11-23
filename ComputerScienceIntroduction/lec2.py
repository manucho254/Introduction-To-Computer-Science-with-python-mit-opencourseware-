#strings

hi = "hello there"

#concatnate strings

name = "ana"
greet = hi + name

greeting = hi + " " + name

silly = hi + " " + name * 3

print(greet)
print(silly)
print(greeting)


#Output Program

x = 1

print(x)

x_str = str(x)

print("my fav num",  x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x = " + x_str)

# input program
#

text = input("Type anything ")
print(5*text)

# change number to interger

text = int(input("Type anything "))
print(5*text)


#indentation
"""
 conditionals if statements
"""

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))

if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x / y is ",  x/y)
        
elif x < y:
    print("x is smaller")
    
else:
    print("Y is smaller")
    
print("thanks!")


"""
 conditionals while loops
"""

n = input("You're in the Lost Forest. Go left or right?")

while n  == "Right":
    n = input("You're in the Lost Forest. Go left or right?")
    
print("you got out of the lost forest")


n = 0 
while n  < 5:
    n = n + 1
    n += 1
    
    
# for loops

for n in range(5):
    print(n)
    
    
mysum = 0

for i in range(7, 10):
    mysum += i
    
print(mysum)

mysum = 0

for x in range(5, 11, 2):
    mysum += x
    
print(mysum)
    
