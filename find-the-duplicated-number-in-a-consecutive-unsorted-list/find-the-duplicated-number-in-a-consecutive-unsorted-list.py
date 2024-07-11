import collections

def find_dup(arr):
    return collections.Counter(arr).most_common(1)[0][0]