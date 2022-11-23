"""
    STRING MANUPILATION, GUESS AND CHECK, APPROCIMATION, BISECTION

"""


# check length of a string

s = "abc"

len(s) # evaluates to 3


def len_(string: str) -> int:
    # O(n) this should run in linear time
    count = 0
    for _ in string: count += 1
    return count

def pow_(a, b):
    return a ** b

print(len_(s))

#slicing

string = "abcdefgh"
print(len_(string))

print(string[3:6]) # evaluates to "def" same as s [3:6:1]
print(string[3:6:2]) # evaluates to "df"
print(string[::]) # evaluates to "abcdefgh" same as s[0:len(s):1]
print(string[::-1]) # evaluates to hgfedbca , same as s[-1:-(len(s)+1):-1]
print(string[4:1:-2]) #evaluates to "ec"

#strings a immutable

t = "hello"
try:
    t[0] = 'y' # returns an error because stringa immutable in python
except TypeError as e:
    print(e)
t = 'y' + t[1:len(s)]

## STRINGS AND LOOPS

v = "abcdefghij"

# works but not pythonic
for index in range(len(v)):
    if v[index] == "i" or v[index] == "u":
        print("There is an i or u")


# more pythonic

for char in v:
    if char == "i" or char == "u":
        print("There is an i or u")
        


