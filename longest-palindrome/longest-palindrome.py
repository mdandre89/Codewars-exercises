def longest_palindrome(s):
    M = 0
    for i in range(0,len(s)+1):
        for j in range(i):
            v = s[j:i]
            if v == v[::-1] and len(v)>M:
                M = len(v)
    return M