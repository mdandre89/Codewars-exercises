def is_twinprime(n):
    return is_prime(n) and (is_prime(n-2) or is_prime(n+2))


from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):    
        if num%i == 0:
            return False
        i += 1
    return True 