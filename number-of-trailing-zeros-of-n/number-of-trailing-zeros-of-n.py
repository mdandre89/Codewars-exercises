from math import log, floor
def zeros(n):
    return sum( floor(n/5**k) for k in range(1, floor(log(n)/log(5))+1) ) if n>1 else 0