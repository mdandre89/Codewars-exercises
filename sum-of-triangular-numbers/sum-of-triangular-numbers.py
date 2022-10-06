def sum_triangular_numbers(n):
    return sum([sum([i for i in range(j+1)]) for j in range(n+1)])