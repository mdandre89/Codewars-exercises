import math
def cartesian_neighbors_distance(x, y, r):
    t = set()
    for i in range(r+1):
        for j in range(i+1):
            t.add(round(math.sqrt(i**2+j**2),10))
    t.remove(0.0)
    return sorted(list(t))