from collections.abc import Iterable
def locate(seq, value):
    if value in seq:
        return True
    seq = flatten(seq)
    return True if value in seq else False


def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el 