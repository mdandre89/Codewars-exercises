def mxdiflg(a1, a2):
    s1 = [len(i) for i in a1]
    s2 = [len(i) for i in a2]
    if a1 == [] or a2 == []:
        return -1
    else:
        return max (abs(max(s1) - min(s2)),abs(max(s2) - min(s1)))
        