def remove(s):
    if (len(s)>0 and s[-1]=="!"):
        return s[:-1]
    else: return s