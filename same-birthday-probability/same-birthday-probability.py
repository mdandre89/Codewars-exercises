import math
def calculate_probability(n):
    f = math.factorial
    if n < 365:
        return round(1 - f(365)/(f(365-n)*(365)**n),2)
    else:
        return 1