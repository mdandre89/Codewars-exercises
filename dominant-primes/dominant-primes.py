def solve(a,b):
    f = factors(b)
    l = sorted(f)
    return sum(j for i,j in enumerate(l) if j>=a and  i+1 in f) 

def factors(n):
    inn = set()
    outn = set()
    for i in range(2,n+1):
        if i not in outn:
            inn.add(i)          
            for j in range(i,n+1,i):
                outn.add(j)
    return inn if inn else {n}