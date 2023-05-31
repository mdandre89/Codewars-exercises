import math
def square_it(digits):
    s = str(digits)
    l = len(s)
    lq = math.sqrt(l)
    return '\n'.join(s[i:i+int(lq)] for i in range(0, l, int(lq))) if lq == int(lq) else "Not a perfect square!"