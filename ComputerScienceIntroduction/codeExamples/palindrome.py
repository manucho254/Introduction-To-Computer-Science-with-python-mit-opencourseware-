def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
                
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and isPal(s[1:-1])
    
    return isPal(toChars(s))

def isPali(s):
    return s == s[::-1]

print(isPali("cooc"))
print(isPalindrome("cooc"))
