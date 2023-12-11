def iq_test(n):
    def df(y):
        if int(y)%2==0:
            return 0
        else:
            return 1            
    s = list(map(df,n.split()))
    if sum(s)>1:
        return s.index(0)+1
    return s.index(1)  +1          