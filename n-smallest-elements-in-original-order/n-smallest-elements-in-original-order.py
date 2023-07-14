def first_n_smallest(arr, n):
    s = sorted(arr)[:n]
    ls = []
    for i in arr:
        if i in s:
            ls.append(i)
            s.remove(i)
    return ls