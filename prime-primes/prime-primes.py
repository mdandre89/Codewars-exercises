from functools import reduce
def prime_primes(n):
    ls = euclide(n)
    return  ((len(ls)-1)*len(ls)//2, int(reduce(lambda x,y:x+sum(ls[:y[0]])/y[1],enumerate(ls),0)))
    

def euclide(n):
    t = []
    s = set()
    for i in range(2,n):
        if i not in s:
            t.append(i)
            for j in range(i,n,i):
                s.add(j)
    return t