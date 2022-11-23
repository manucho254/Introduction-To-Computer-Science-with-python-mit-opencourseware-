# find fibonacci numbers efficient

def fib_efficient(n, d):
    if n in d:
        return d[n]
    ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
    d[n] = ans
    
    return ans

d = {1:1, 2:2}

print(fib_efficient(11, d))