def total(arr):
    l = len(arr)
    return sum(arr[i] for i in factors(l-1)) if l >0 else 0


def factors(n):
    inn = set()
    outn = set()
    for i in range(2,n+1):
        if i not in outn:
            inn.add(i)          
            for j in range(i,n+1,i):
                outn.add(j)
    return inn if inn else {n}