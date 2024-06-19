from functools import reduce
from operator import mul
from itertools import combinations
def get_num(arr):
    t = set()
    s = (set(reduce(mul,i) for i in combinations(arr, i)) for i in range(1,len(arr)+1))
    return [reduce(mul, arr),len(t.union(*s)),min(arr),reduce(mul, sorted(arr)[1:])]