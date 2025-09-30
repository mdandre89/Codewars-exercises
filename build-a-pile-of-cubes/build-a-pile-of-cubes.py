from math import sqrt
from decimal import Decimal
def find_nb(m):
    n = Decimal(sqrt(1+8*sqrt(m)))
    z = (-1+n)/2
    if (z*(z+1)/2)**2==m:
        return z
    return -1