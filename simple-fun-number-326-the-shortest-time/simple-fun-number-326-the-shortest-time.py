def shortest_time(n,m,speeds):
    if n == 1:
        return 0
    sec = abs(m-n)*speeds[0] + abs(n-1)*speeds[0] + 2*speeds[1]+ speeds[2]
    walk = abs(n-1)*speeds[3]
    return sec if sec<walk else walk