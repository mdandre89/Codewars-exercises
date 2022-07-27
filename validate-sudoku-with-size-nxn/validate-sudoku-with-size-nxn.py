from math import sqrt
class Sudoku(object):
    def __init__(self,board):
        self.board = board
        
    def is_valid(self):
        l = len(self.board)
        if len(self.board) == 1 and self.board[0][0] not in [0,1] or str(self.board[0][0])=="True":
            return False
        def row_ver(self):
            for i in self:
                for j in range(1,l+1):
                    if i.count(j)!=1:
                        return False
            return True

        def ver3(self):
            l = len(self)
            st = int(sqrt(l))
            ls = []
            for z in range(0,l,st):
                for i in range(l):
                    for j in range(0,l,st):
                        ls.append(self[i][z+j//st+j%st])
            return [ls[i:i+l] for i in range(0,len(ls),l)] 
        
        if row_ver(self.board) and row_ver(zip(*self.board)):
            return row_ver(ver3(self.board))
        return False