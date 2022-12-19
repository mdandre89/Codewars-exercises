def minesweeper(matrix):
    l = len(matrix)
    l1 = len(matrix[0])
    t = [[0]*l1 for i in range(l)]
    for i in range(l):
        for j in range(l1):
            t[i][j] = counta(i,j,matrix)
    return t
    
    
def counta(i,j, matrix):
    s = 0
    for z in [-1,0,1]:
        for k in [-1,0,1]:
            try:
                if i+z>=0 and j+k>=0:
                    s+= matrix[i+z][j+k]
            except:
                pass
    return s if matrix[i][j] == 0 else s-1