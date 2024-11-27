def sum_diagonals(matrix):
    return sum(matrix[i][i] + matrix[i][len(matrix)-i-1] for i in range(0, len(matrix))) if matrix!=[[]] else 0