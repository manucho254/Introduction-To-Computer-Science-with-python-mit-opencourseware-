# tuples

def get_data(aTuple):
    nums = ()
    words = ()
    
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    
    min_n = min(nums)
    max_n = max(nums)
    
    unique_words = len(words)
    
    return (min_n, max_n, unique_words)


print(get_data(((2014, "katy"), (2014, "harry"), (2012, "Jake"))))


def r_(arr: list, val: str) -> list:
    if len(arr) == 0:
        return False
    
    mid = len(arr) // 2
    
    if val == arr[mid]: return arr[mid]
    
    if arr[mid] < val: return r_(arr[mid+1:], val)
    
    return r_(arr[:mid-1], val)

print(r_(["apple", "boy", "cat", "dog", "egg", "full", "pan", "test", "van", "zip"], "zip"))



def merge_sort():
    pass

    
