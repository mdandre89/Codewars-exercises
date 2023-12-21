def atomic_number(num):
    s=0
    t=[]
    i=1
    while s<num:
        s+=2*i**2;
        if(s<num):
            t.append(2*i**2)
        else:
            t.append(num-sum(t))
        i+=1
    return t