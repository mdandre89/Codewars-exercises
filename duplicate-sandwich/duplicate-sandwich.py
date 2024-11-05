def duplicate_sandwich(arr):
    s = set()
    ls = []
    for i in arr:
        if i in s:  
            return ls[ls.index(i)+1:]
            break
        else:
            s.add(i)
            ls.append(i)
    return ls