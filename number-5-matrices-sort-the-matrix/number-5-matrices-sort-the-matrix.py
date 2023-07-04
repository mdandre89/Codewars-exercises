def order(matrix):
    return [list(i) for i in zip(*(sorted(i) for i in zip(*(sorted(i) for i in matrix))))]