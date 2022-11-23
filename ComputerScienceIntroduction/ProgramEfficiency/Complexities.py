"""
  Quadratic complexity O(n2)
"""

def isSubset(l1, l2):
    for el in l1:
        matched = False
        for e2 in l2:
            if el == e2:
                matched = True
                break
        if not matched:
            return False
        
    return True

print(isSubset([1, 2, 3], [1, 2, 3]))
print(isSubset([1, 4, 3], [1, 2, 3]))

"""   
  Find intersect O(n2)
"""

def intersect(L1, L2):
    tmp = []
    for el in L1:
        for e2 in L2:
            if el == e2:
                tmp.append(el)
                
    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)
            
    return res
    
print(intersect([1, 2, 3], [1, 2, 3]))
print(intersect([1, 4, 3], [1, 2, 3]))