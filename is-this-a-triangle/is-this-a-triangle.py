def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a+b<=c or b+c<=a or c+a<=b:
        return False
    return True
    