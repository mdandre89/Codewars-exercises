def fold_array(arr, runs):
    i = 0
    while i < runs:
        arr = fold(arr)
        i+=1
    return arr
        
def fold(ar):
    l = len(ar)
    if l % 2 == 1:
        return [ar[i] + ar[l-i-1] for i in range(l//2)] + [ar[l//2]]
    else:
        return [ ar[i] + ar[l-i-1] for i in range(l//2)]