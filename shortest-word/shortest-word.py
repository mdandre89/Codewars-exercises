def find_short(s):
    s=s.split()
    s.sort(key=len)
    return len(s[0])