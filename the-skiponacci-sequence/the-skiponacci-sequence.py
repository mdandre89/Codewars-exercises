cache = {0: 0, 1: 1}

def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]

def skiponacci(n):
    s = ''
    for i in range(1, n+1):
        if i%2 == 0:
            s += ' skip '
        else:
            s += str(fibonacci_of(i))
    return s.strip()