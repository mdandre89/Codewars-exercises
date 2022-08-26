import re
def isSolved(board):
    b = 'z'.join(''.join(str(j) for j in i)  for i in board)
    b1 = 'z'.join(''.join(str(j) for j in i)  for i in zip(*board))
    for i in {'1','2'}:
        rex = i+'{3}'
        if re.search(rex,b) or b[0]==b[5]==b[10]==i or b[2]==b[5]==b[8]==i or re.search(rex,b1):
            return int(i)
    return -1 if '0' in b  else 0 