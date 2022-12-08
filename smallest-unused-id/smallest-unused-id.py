def next_id(arr):
    s = set(arr)
    m = max(s or [0])
    for i in range(0, max(m+2,2)):
        if i not in s and i>=0:
            return i