def winner(st, jo):
    g = ''.join('0' if '23456789TJQKA'.index(i[0])<'23456789TJQKA'.index(i[1]) else '1' for i in filter(lambda x : x[0]!=x[1],zip(st,jo)))
    m,n,t  = g.count('0'), g.count('1'), 1 if  g.count('0')> g.count('1') else 0
    return "{} wins {} to {}".format(['Steve','Josh'][t],max(m,n),min(m,n)) if m!=n else 'Tie'