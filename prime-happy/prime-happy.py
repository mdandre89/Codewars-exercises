from math import sqrt
def is_prime_happy(n):
    if n == 0:
        return False
    return (5 + sum(i+1 for i in range(6,n,6) if is_prime(i+1)) + sum(i-1 for i in range(6,n,6) if is_prime(i-1)) )%n == 0 

def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):    
        if num%i == 0:
            return False
        i += 1
    return True 