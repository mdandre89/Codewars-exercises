import math
class Sudoku(object):
    def __init__(self, data):
        self.data = data
    def is_valid(self):
        n, m = len(self.data), int(math.sqrt(len(self.data)))
        if type(self.data[0][0]) == bool: return False
        for i in self.data:
            if set(i) != set(range(1,n+1)):
                return False
        for i in zip(*self.data):
            if set(i) != set(range(1,n+1)):
                return False
        ls = [[list(zip(*i))[j:j+m] for j in range(0,n,m)] for i in [self.data[i:i+m] for i in range(0,n,m)] ]
        for a in [i for sub in ls for i in sub]:
            if set([i for sub in a for i in sub]) != set(range(1,n+1)):
                return False
        return True
