def divisors(n):
    return sum(1 for j in range(1,n+1) if n%j==0)