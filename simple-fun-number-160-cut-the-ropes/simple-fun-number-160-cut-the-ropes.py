def cut_the_ropes(arr):
    l = len(arr)
    t = []
    while sum(arr)!=0:
        n = min([i for i in arr if i>0])
        t.append(l-arr.count(0))
        arr = [i - n if i>0 else 0 for i in arr ]
    return t