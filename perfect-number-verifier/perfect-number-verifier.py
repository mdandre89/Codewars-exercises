#Should return whether or not n is a perfect number
def isPerfect(n):
    tot=1
    d=2
    j=n/2+1
    while d<j:
        if n%d==0: 
            tot= tot+n/d + d 
        d+=1
        j=n/d
    if n==1: return False
    return tot==n    