from collections import Counter as d
def common(a,b,c):
    return sum(i*j for i,j in (d(a) & d(b) & d(c)).items())