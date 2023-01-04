import functools
def gcd_rec(a, b): 
    if b:
        return gcd_rec(b, a % b)
    else:
        return a

def mn_lcm(m,n):
  return functools.reduce(lambda a,b : a*b/gcd_rec(a,b), range(min(n,m),max(n,m)+1) ) 