import math
def largestPower(N):
    i=0
    while i<math.log(N,3):
        i+=1
    return i-1