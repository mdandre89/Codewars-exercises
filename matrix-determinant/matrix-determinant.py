def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    if len(matrix)==2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    s = 0
    for i,j in enumerate(matrix[0]):
        s += j*((-1)**(i%2))*determinant([z[:i]+z[i+1:] for z in matrix[1:]])
    return s