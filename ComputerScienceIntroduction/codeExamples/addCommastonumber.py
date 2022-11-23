my_str = "1000000058380"
arr = []

for i, x in enumerate(my_str[::-1]):
    if i % 3 == 0: arr.append(",")
    arr.append(x)
        
print("".join(arr[::-1])[:-1])