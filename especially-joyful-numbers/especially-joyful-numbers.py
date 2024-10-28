def numberJoy(n):
    m = sum([int(i) for i in str(n)])
    if m*int(str(m)[::-1]) == n:
        return True
    return False