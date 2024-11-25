import functools, math
def find_difference(a, b):
    return abs(functools.reduce(lambda x,y:x*y,a)-functools.reduce(lambda x,y:x*y,b))