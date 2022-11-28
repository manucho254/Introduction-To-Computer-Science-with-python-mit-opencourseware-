"""
    Logarithmic function O(log n)
""" 

def intToStr(i):
    digits = "0123456789"
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = 1 // 10
        
    return result

print(intToStr(98))