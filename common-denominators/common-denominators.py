import functools, math
def convertFracts(lst):
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
    
    return [[numos[i]*math.floor(lcmm(denos)/denos[i]),lcmm(denos)] for i in range(0,l)]