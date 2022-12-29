from math import sqrt
def triangular_sum(n):
    return  sqrt((sqrt(1+8*n)-1)/2)%1==0