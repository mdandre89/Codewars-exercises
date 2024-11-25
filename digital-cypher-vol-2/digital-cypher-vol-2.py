from itertools import cycle
import string
def decode(code, key):
    itera = cycle(str(key))
    return "".join(string.ascii_lowercase[n-1] for n in [i -int(next(itera)) for i in code])