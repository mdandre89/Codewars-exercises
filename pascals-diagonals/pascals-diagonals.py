def generate_diagonal(n, l):
    i = 2
    t = [1]
    while i <= l:
        t.append(t[-1]*(i+n-1)//(i-1))
        i += 1
    return t if l >0 else []