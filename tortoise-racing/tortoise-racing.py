import math 
def race(v1, v2, g):
    h,m = divmod(g/(v2-v1)*60, 60)
    m,s  = divmod(m*60, 60)
    return None if v1>=v2 else [h, m, math.floor(s)]
    