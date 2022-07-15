import re
def in_array(array1, array2):
    t = []
    for i in a1:
        for j in a2:
            if re.search(i,j):
                t.append(i)
    t = sorted(list(set(t)))               
    return t