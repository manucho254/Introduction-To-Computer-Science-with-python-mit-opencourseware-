 
def remove_dups(l1: list, l2 : list) -> None:
    """ Wrong implimentation """
    for e in l1:
        if e in l2:
            l1.remove(e)
    
L1 = [1, 2, 3, 4]
L2 = [1, 2, 3, 4]

remove_dups(L1, L2)

print(L1)
print(L2)


def remove_dup(l1: list, l2 : list) -> None:
    """ correct implimentation """
    l1_copy = l1[:] # create a copy of the list
    for e in l1_copy : 
        if e in l2: 
            l1.remove(e)
            
L1 = [1, 2, 3, 4]
L2 = L1[:]

remove_dup(L1, L2)

print(L1)
print(L2)
