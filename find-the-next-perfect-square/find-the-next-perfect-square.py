def find_next_square(sq):
    from math import sqrt
    return (sqrt(sq) + 1) ** 2 if sqrt(sq).is_integer() else -1