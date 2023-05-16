def on_line(p):
    print(p,len(p))    
    if len(p) <=1:
        return True
    p1,p2 = p[0:2]
    try:
        c = (p2[0] - p1[0]+0.0)/(p2[1] - p1[1])
    except:
        try:
            c = p1[1]
        except:
            return True
    for i in p[2:]:
        try:
            if c != (i[0] - p2[0]+0.0) / (i[1] - p2[1]):
                return False
        except:
            if c != i[1]:
                return False
    return True