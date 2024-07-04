def find_outlier(integers):
    t = [1 if i%2==1 else 0 for i in integers]
    return integers[t.index(0)]  if t.count(1)>1 else integers[t.index(1)]