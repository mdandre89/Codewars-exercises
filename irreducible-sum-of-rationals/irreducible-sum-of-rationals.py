import functools,decimal,math

def sum_fracts(lst):
    decimal.getcontext().prec = 100
    if lst==[]:
        return None
    print(lst)
    l = len(lst)
    denos = [j[1] for j in lst]
    numos = [j[0] for j in lst]
    
    def gcd(a, b):
        while b:      
            a, b = b, a % b
        return a
        
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    def lcmm(*args):
        return functools.reduce(lcm, *args)
    
    lst2 = [numos[i]*math.floor(lcmm(denos)/denos[i]) for i in range(0,l)]
    return  [int(decimal.Decimal(sum(lst2))/gcd(sum(lst2),lcmm(denos))), math.floor(lcmm(denos)/gcd(sum(lst2),lcmm(denos)))] if lcmm(denos)/gcd(sum(lst2),lcmm(denos)) !=1 else sum(lst2)/gcd(sum(lst2),lcmm(denos)) 