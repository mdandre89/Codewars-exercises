dictio = {}
from decimal import *
from math import factorial

def routes(n):
    if n <= 0:
        return 0
    s = summa(n, n)
    return s
    
def summa(n,m):
    if m == 0:
        return 1
    if m == 1:
        return n + 1
    if str(n)+str(m) in dictio:
        return dictio[str(n)+str(m)]
    else:
        dictio[str(n)+str(m)] = factorial(n + m) //  (factorial(n) * factorial(m) ) 
        dictio[str(m)+str(n)] = dictio[str(n)+str(m)]
        return dictio[str(n)+str(m)]
 