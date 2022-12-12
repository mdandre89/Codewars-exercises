def solve(s):
    if s == s[::-1] : return "OK"
    for i in range(0,len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1] : return "remove one"
    return "not possible"