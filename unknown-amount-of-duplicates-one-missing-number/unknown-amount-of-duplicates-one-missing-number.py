from collections import Counter as c 
def find_dups_miss(arr):
    dictio = c(arr)
    s = set(arr)
    mi,ma = min(s), max(s)
    g = ma*(ma+1)/2 - mi*(mi-1)/2 -sum(s)
    return [g,sorted((i for i in dictio if dictio[i]>1))] 