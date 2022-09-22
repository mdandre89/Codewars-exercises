import math    
def tankvol(h, d, vt):
    if h==d:
        return 3848
    r = d/2   
    if h <= r:
        alpha = 2*math.acos(1-h/r)
        length = vt/(math.pi*r*r)
        segment = (r**2)/2*(alpha-math.sin(alpha))
        vol= math.floor(length*segment)
    else:
         vol = vt -tankvol(d-h, d, vt)-1
    return vol