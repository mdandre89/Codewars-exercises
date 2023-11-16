ROW={"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
def knight_vs_king (knight, king):
    if abs(knight[0] - king[0]) <=1 and abs(ROW[knight[1]] - ROW[king[1]]) <= 1:
        return "King"
    elif abs( knight[0] - king[0] )*abs( ROW[knight[1]] - ROW[king[1]] ) == 2:
        return "Knight"
    else:
        return "None"