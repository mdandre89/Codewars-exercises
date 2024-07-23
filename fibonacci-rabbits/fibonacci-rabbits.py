def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function
@memoize    
def fib_rabbits(n, b):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    return  fib_rabbits(n-1,b) + b*fib_rabbits(n-2,b)