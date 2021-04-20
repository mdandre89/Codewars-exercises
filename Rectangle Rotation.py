from math import sqrt
def rectangle_rotation(a, b):
    n = 2*int(a/(2*sqrt(2)))+1
    m = 2*int(b/(2*sqrt(2)))+1
    n1 = 2*int((a/2-sqrt(2)/2)/sqrt(2)+1)
    m1 = 2*int((b/2-sqrt(2)/2)/sqrt(2)+1)
    return n*m + n1*m1
