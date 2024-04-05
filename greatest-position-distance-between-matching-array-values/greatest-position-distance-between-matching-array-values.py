from collections import Counter as c
def greatest_distance(arr):
    M = 0
    ls = (i[0] for i in c(arr).items() if i[1]>1)
    for i in ls:
        m =  len(arr)- arr[::-1].index(i) - arr.index(i) -1
        if m > M:
            M =m
    return M  