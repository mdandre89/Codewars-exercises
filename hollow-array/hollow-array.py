def is_hollow(x):
    l = len(x)
    c = 0
    if x[l//2-1: l//2+2] != [0, 0, 0]:
        return False
    for i in range(l//2):
        if bool(x[i]) != bool(x[l-1-i]):
            return False
    return True