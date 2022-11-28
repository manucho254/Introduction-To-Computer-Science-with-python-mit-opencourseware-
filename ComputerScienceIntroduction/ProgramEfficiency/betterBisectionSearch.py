"""Better bisection search implementation
  O(log n)
"""

def bisection_search(L, e):
    def bisection_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        
        mid = (low + high) // 2
        
        if L[mid] == e:
            return True
        
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisection_search_helper(L, e, low, mid - 1)
        else:
            return bisection_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisection_search_helper(L, e, 0, len(L) - 1)
    
    
print(bisection_search([x for x in range(1, 10001)], 500))
    
    