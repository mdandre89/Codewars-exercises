def bishop_and_pawn(b, p):
    strng = "abcdefgh"
    return  abs(strng.index(b[0]) - strng.index(p[0]))  == abs(int(b[1]) - int(p[1]))