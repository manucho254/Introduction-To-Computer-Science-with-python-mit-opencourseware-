"""
  Tuples, Aliasing, Mutability and cloning
"""

my_tup = (1, 2, 3, 4, 5, 6, 7)

print(my_tup[::-1])

#swap values with tuples

x = 2
y = 4

(x, y) = (y, x)

print(x, y)


def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    
    return (q, r)

(quot, rem) = quotient_and_remainder(4, 5) 

print(quot, rem)


#lists

L = [2, 1, 3, 6, 3, 7, 0] #do below
L.append(5) # -> add 5 to list
print(L)
L.remove(2) # -> mutates L = [1, 3, 6, 3, 7, 0]
L.remove(3) # -> mutates L = [1, 6, 3, 7, 0]
del(L[1]) # -> mutates L = [1, 3, 7, 0]
L.pop() # -> mutates L = [1, 3, 7, 0]
print(L) # -> return 0 and mutates L


# strings to lists and list to string

s = "I<3 cs"  # -> s is a string
list(s) # -> returns ['I', '<', '3', ' ', 'c', 's']
s.split('<') # returns ['I', '3 cs']
L = ['a', 'b', 'c'] # L is a list
''.join(L) # returns "abc"
'_'.join(L) # returns "a_b_c"


# sorting lists

L = ['a', 'b', 'c']

sorted(L) # returns sorted list and does not mutate L
L.sort() # mutates L = ['a', 'b', 'c']
L.reverse() # mutates L = ['c', 'b', 'a']


warm = ['red', 'yellow', 'orange']
hot = warm
hot.append('pink')
print(hot)
print(warm)

# Cloning a list

cool = ['blue', 'green', 'grey']
chill = cool[:]
chill.append('black')
print(chill)
print(cool)

# more on sorting lists

warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print(warm)
print(sortedwarm)

# Cloning a list

cool = ['blue', 'green', 'grey']
sortedcool = sorted(cool)
print(chill)
print(sortedcool)


dict_ = {"test": 12747, "test2": 10}

data = sorted(dict_.values())