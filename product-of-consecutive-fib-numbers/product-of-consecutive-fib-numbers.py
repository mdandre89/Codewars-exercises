def productFib(prod):
    def fib(n, computed = {0: 0, 1: 1}):
        if n not in computed:
            computed[n] = fib(n-1, computed) + fib(n-2, computed)
        return computed[n]
    y = 1
    while fib(y) <= prod/fib(y):
        if  fib(y+1)*fib(y+2) == prod:
            return [fib(y+1), fib(y+2), True]
        elif fib(y+1)*fib(y+2) > prod:
            return [fib(y+1), fib(y+2), False]
        else:
            y += 1 
            
        