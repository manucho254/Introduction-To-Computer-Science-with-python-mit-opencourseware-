""" 
   Bubble sort algorithm O(n2) Quadratic
"""

def bubble_sort(L):
    swap = False
    
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
        
    return L
                
print(bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
            