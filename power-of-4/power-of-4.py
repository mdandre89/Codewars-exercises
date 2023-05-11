from math import log
def powerof4(n):
    return (log(n)/log(4)) % 1 == 0 if type(n) == int and n > 0 else False