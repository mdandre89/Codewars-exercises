from math import sqrt
def closest_points3D(pointsL):
    s1 = len(pointsL)
    s2 = []
    L = sqrt((pointsL[0][0]-pointsL[1][0])**2+(pointsL[0][1]-pointsL[1][1])**2+(pointsL[0][2]-pointsL[1][2])**2)
    for i in range(s1):
        for j in range(i):
            d = round(sqrt((pointsL[i][0]-pointsL[j][0])**2+(pointsL[i][1]-pointsL[j][1])**2+(pointsL[i][2]-pointsL[j][2])**2),5)
            if d<=L:
                s2.append([[pointsL[i],pointsL[j]],d])
    s2 = sorted(s2,key=lambda x: x[1]) 
    return [s1,[sorted(s2[0][0],key=lambda x: (x[0],x[1],x[2]))],s2[0][1]]