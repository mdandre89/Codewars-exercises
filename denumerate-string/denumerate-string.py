def denumerate(ls):
    try:
        l = range(len(ls))
        for i in ls:
            if type(i)!=tuple or not i[1].isalnum() or len(i)!=2 or len(i[1])!=1 or i[0] not in l:
                return False
        s = "".join(i[1] for i in sorted(ls, key=lambda x: x[0]))
    except:
        return False
    return s