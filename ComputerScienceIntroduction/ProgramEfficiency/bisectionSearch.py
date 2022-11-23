""" bisection search runs in n logarithmic time O(n log n)"""


def bisect_search(L, e):
    if L == []:
        return False
    
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search(L[:half], e)
        else:
            return bisect_search(L[half:], e)
        

print(bisect_search([x for x in range(1, 10000001)], 500))