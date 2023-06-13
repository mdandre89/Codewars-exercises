def group(arr):
    t = []
    s =[]
    for i in arr:
        if i not in s:
            t.append([i]*arr.count(i))
            s.append(i)
    return t