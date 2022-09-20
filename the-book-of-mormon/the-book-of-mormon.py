import math
def mormons(n, r, t):
    i = 0 
    while n*(1+r)**i <t:
        i+=1
    return i