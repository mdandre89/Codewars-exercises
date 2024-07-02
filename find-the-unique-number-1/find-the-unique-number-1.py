import collections
def find_uniq(arr):
    c = collections.Counter(arr)
    return c.most_common()[-1][0]