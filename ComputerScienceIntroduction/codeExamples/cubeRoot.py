"""
  Find the cube root of a number
"""

cube = 8

for guess in range(cube+1):
    if guess ** 3 == cube:
        print("cube root of", cube, "is", guess)
        
        
# more comprehensive example
 
for guess in range(abs(cube)+1):
    if guess ** 3 >= abs(cube):
        break
    
if guess ** 3 != abs(cube):
    print(cube, "is not a perfect cube")
    
else:
    if cube < 0:
        guess = -guess
    print("Cube root of " + str(cube) + ' s '+ str(guess))
    
    
    
# find cube roo by approximation

cube = 27
cube = 8120601
cube = 10000
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    print(guess)
    guess += increment
    num_guesses += 1
    
print('num_guesses = ', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to the cube root of ", cube)
    
