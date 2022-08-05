from math import factorial
def uniq_count(e):
    e = str(e).upper()
    n = factorial(len(e))
    for i in (e.count(i) for i in set(e) if e.count(i)>1):
        if i:
            n = n // factorial(i)
    return n