class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = "\n".join("0"*self.width for i in range(self.height))
        
    def __repr__(self):
        return self.grid
    
    def plot_point(self, x, y):
        ls = "\n".join("0"*(x-1) + "X" + "0"*(self.width -x) if i==y-1 else j for i,j in enumerate(self.grid.split("\n")))
        self.grid = ls
        return self.grid