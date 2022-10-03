def summary_ranges(args):
    if args == []: return []
    args = sorted(set(args))
    s = []
    t = []
    M = args[-1]+1
    for i in args:
        if i in s:
            pass
        else:
            for j in range(i+1,M+1):
                s = range(i,j)
                if j in args:
                    pass
                elif  i!=j-1:
                    t.append("->".join([str(s[0]),str(s[-1])]))
                    break
                else:
                    t.append(str(i))
                    break
    return t