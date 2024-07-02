import re
def find_uniq(arr):
    arr = [i for i in arr if i!=""]
    sa = "".join(sorted(list(set(list(arr[0].lower())))))
    ls2 = list(filter(lambda x: sa not in "".join(sorted(set(list(x.lower())))), arr))
    return ls2[0] if len(ls2) == 1 else arr[0]