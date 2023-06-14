def ordered_count(input):
    t=[]
    for j in input:
        if j not in [i[0] for i in t]:
            t.append((j,input.count(j)))
            
    return t