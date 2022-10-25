def validSolution(board):
    return row_ver(board) and row_ver(zip(*board)) and row_ver(ver3(board))
    
def row_ver(boards):
    for i in boards:
        for j in range(1,10):
            if i.count(j)!=1:
                return False
    return True
    
def ver3(board):
    ls = []
    for z in range(0,9,3):
        for i in range(9):
            for j in range(0,9,3):
                ls.append(board[i][z+j//3+j%3])
    return [ls[i:i+9] for i in range(0,len(ls),9)]            