def divisors(n):
    t = [i for i in range(2,n//2+1) if n%i==0]
    return t if t else str(n) + ' is prime'