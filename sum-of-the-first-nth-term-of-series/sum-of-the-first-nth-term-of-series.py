import math
def series_sum(n):
    sum= j=0 
    while j<n:
        sum += 1/(1+3*j)
        j+=1
    return "{:04.2f}".format(sum,2)  if n>0 else "0.00"