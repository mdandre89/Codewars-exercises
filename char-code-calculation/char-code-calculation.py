def calc(x):
    return sum([6 if '7' in str(ord(y)) else 0 for y in x])