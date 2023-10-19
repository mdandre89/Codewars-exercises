def bingo(ls,win):
    return    ['Loser!','Winner!'][sum(chr(i[1]) in i[0] for i in ls) >= win]