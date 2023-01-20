import math
def solve(a,b):
    return all(int(a)%i==0 for i in factors(int(b)))
            
def factors(n):
    inn = set()
    outn = set()
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0 and i not in outn:
            inn.add(i)          
            for j in range(i,int(math.sqrt(n))+1,i):
                outn.add(j)
    return inn if inn else [n]
                