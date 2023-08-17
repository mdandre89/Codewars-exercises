import math

def count_of_heads(initial, n, swings):
    if swings == 1:
        return initial - 1 + math.factorial(swings)*n
    else:
        return count_of_heads(initial, n, swings-1) - 1 + math.factorial(swings)*n