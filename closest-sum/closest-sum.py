from itertools import combinations
def closest_sum(ints, num):
    ls = sorted([sum(i) for i in combinations(ints,3)])
    m  = min([abs(i-num) for i in ls])
    return m + num if m + num in ls else -m + num    