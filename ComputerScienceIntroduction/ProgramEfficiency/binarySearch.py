
""" 
    binary search O(log n)
    The list must be sorted for this to work
"""

def binary_search(L,  e):
    if len(L) == 0:
        return False
    
    mid = len(L) // 2
    
    if L[mid] == e:
        return True 
    
    if L[mid] < e:
        return binary_search(L[mid+1:], e)
    
    return binary_search(L[:mid], e)


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

