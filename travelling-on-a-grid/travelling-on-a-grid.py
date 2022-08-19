def travel_chessboard(s):
    coorda = [int(s[1]),int(s[3])]
    coordb = [int(s[6]),int(s[8])]
    return summa(coordb[0]-coorda[0], coordb[1]-coorda[1])
    
def summa(n,m):
    n, m = max(n,m), min(n,m)
    if m == 0:
        return 1
    if m == 1:
        return n + 1
    return sum([summa(i,m-1) for i in range(1,n+1)]) +1