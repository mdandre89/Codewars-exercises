import math
def operation(a,b):
    j = 0
    while bin(a)[2:].count("1")>1:
        a = a >> 1
        j+=1
    return  abs(math.log2(a) - math.log2(b))+j