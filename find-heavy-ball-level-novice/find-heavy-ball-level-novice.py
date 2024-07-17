def find_ball(scales):
    t = scales.get_weight([0,1,2],[3,4,5])
    if t:
        t = [0,1,2] if t == -1 else [3,4,5] 
        s = scales.get_weight([t[0]],[t[1]])
        print('b')
        if s:
            return t[0] if s == -1 else t[1]
        else:
            return t[2]
    return 6 if scales.get_weight([6],[7])==-1 else  7