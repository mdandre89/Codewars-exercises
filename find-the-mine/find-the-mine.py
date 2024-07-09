def mineLocation(field):
     return [[i, j] for i in range(len(field)) for j in range(len(field[i])) if field[i][j] == 1][0]