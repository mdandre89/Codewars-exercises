SQ = 2**0.5
def rectangle_rotation(a, b):
    a,b = max(a,b), min(a,b)
    na, nb = (a/2)//SQ, (b/2)//SQ
    na2, nb2 = ((a/2)+SQ/2)//SQ, ((b/2)+SQ/2)//SQ  
    return  (2*na+1)*(2*nb+1) + na2*nb2*4