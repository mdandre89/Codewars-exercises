import math
def add(*args):
    return round(sum(j/(i+1) for i,j in enumerate(args))) if args else 0