"""  
   Selection sort O(n2)
"""

def selection_sort_(n: list):
    suffix_st = 0
    while suffix_st != len(n):
        print("selection sort: ", str(n))
        for i in range(suffix_st, len(n)):
            if n[i] < n[suffix_st]:
                n[suffix_st], n[i] = n[i], n[suffix_st]
        suffix_st += 1
        
    return n

print(selection_sort_([9, 8, 7, 6, 5, 4, 3, 2, 1]))