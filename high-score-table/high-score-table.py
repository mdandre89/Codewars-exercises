class HighScoreTable:
    
    def __init__(self,n):
        self.scores = []
        self.n = n
    
    def update(self,new):
        self.scores = sorted(self.scores+[new])[::-1][:self.n]
    
    def reset(self):
        self.scores = []