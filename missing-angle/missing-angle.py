import math
def missing_angle(h, a, o):
    if h == 0:
        r = math.sqrt(a**2 + o**2)
        return int(round(math.acos(a/r)*180/math.pi))   
    if a == 0:
        return int(round(math.asin(o/h)*180/math.pi))
    if o == 0:
        return int(round(math.acos(a/h)*180/math.pi))