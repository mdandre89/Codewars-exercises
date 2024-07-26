from math import  floor, pi,log1p

def count(n):
    return floor((log1p(2*pi*n-1)/2+n*(log1p(n-1)-1))/log1p(10-1))+1