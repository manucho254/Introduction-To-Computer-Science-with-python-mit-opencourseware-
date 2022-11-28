"""" 
    Exponential complexity O(2n)
"""


def gen_subsets(L):
    if len(L) == 0: 
        return [[]] #list of empty list
    
    smaller = gen_subsets(L[:-1]) # all subsets without last element
    
    extra = L[-1:] #create a list of just the last element 
    
    new = []
    
    for small in smaller:
        new.append(small+extra) # for all smaller solution add one with last element 
        
    return smaller+new # combine those with last element and those without


nums = [3, 3, 1, 2]
print(gen_subsets(nums))

for i in gen_subsets(nums):
    if sum(i) == 6:
        for x in i:
            nums.index
