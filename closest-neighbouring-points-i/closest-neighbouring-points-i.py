from math import sqrt
from itertools import combinations 
def closest_points(pointsL):
    pairs = [list(i) for i in combinations(pointsL,2)]
    distances = [[i,round(sqrt((i[0][0]-i[1][0])**2+(i[0][1]-i[1][1])**2),4)] for i in pairs]
    minid = sorted(distances,key=lambda x: (x[1]))[0][1]
    distances = sorted([sorted(i[0],key=lambda x:(x[0],x[1])) for i in distances if i[1]==minid],key=lambda x:x[0])
    return [len(pointsL),distances,minid]