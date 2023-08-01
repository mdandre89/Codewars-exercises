def accum(s):
    return '-'.join([(s[i]*(i+1)).capitalize() for i in range(0,len(s))])