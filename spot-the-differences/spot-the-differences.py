def spot_diff(s1, s2):
    t=[]
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            t.append(i)
    return t
        