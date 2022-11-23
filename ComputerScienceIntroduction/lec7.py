"""
  Testing, Debugging, Exceptions and Assertions
"""

import unittest

class Testing(unittest.TestCase):
    
    
    def test_equals(self):
        fun = None
        self.assertIsNone(fun)
  
"""
  Exceptions
"""

try:
  n = int(input("Enter value n \n"))
  p = int(input("Enter value p \n"))
  print("n/p = ", n/p)
  print("n+p = ", n+p)
except ValueError:
  print("Could not convert to a number")
except ZeroDivisionError:
  print("Can't divide by zero")
except:
  print("Something went very wrong")
  
  
""" 
 Example of raising an Exception
"""

def get_ratios(l1, l2):
  """
   Assumes: l1, l2  are lists pf equal length of numbers
   Returns: a list containing l1[i]/l2[i]
  """
  ratios = []
  
  for index in range(len(l1)):
    try:
      ratios.append(l1[index]/l2[index])
    except ZeroDivisionError:
      ratios.append(float('nan')) # nan = not a number)
    except:
      raise ValueError('get_ratios called with bad arg')
    
  return ratios

print(get_ratios([0, 2, 3, 4, 5], [1, 2, 3, 4, 5]))

#add  a value to list

def get_stats(class_list):
  new_stats = []
  for elt in class_list:
    new_stats.append([elt[0], elt[1], avg(elt[1])])
  
  return new_stats
    
def avg(grades):
  # catching the exception
  try:
    return sum(grades) / len(grades)
  except ZeroDivisionError:
    print("Warning: no grades data")
    return 0.0

class_list = [[['peter', 'parker'], [80.0, 70.0]],
              [['bruce', 'wayne'], [100.0, 80.0]]]

print(get_stats(class_list))