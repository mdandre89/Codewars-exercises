import functools
def dig_pow(n, p):
    s = sum([int(j)**(p+i) for i,j in enumerate(str(n))])
    return s//n if s//n *n==s else -1