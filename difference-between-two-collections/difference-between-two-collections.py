# return a sorted set with the difference
def diff(a, b):
    return sorted(list(set(a) ^ set(b)))