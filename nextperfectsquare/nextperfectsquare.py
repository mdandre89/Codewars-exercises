from math import sqrt as s
def next_perfect_square(n):
    return (int(s(n)) + 1 )**2 if n>=0 else 0