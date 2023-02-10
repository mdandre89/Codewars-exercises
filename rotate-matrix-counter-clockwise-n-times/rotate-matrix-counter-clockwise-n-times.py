def rotate_against_clockwise(matrix, times):
    times = times%4
    for i in range(4-times):
        matrix = [list(i) for i in zip(*matrix[::-1])]
    return matrix