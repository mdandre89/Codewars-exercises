def findSquares(x,y):
    return sum((x-i+1)*(y-i+1)for i in range(1,y+1))