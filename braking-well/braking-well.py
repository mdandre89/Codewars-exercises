import math
def dist(v, mu):
    v = v/3.6
    return   v + v*v/(2*mu*9.81)

def speed(d, mu):
    return   ( -mu*9.81 + math.sqrt( (mu*9.81)**2 + 2*mu*9.81*d) )*3.6