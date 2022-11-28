"""
  Linear search O(n)
  can work on both sorted and unsorted list/arrays
"""

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

print(linear_search([1, 2, 6, 7, 9, 4, 8, 5], 8))


""" Linear on sorted list O(n)"""

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
        if L[i] > e:
            return False
    return found


print(linear_search([1, 2, 6, 7, 9, 4, 8, 5], 8))
