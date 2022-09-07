def meeting(rooms, n):
    t = []
    for i in rooms:
        if sum(t) == n and n>0:
            return t
        if i[1]-i[0].count("X")>-1:
            t.append(min(i[1]-i[0].count("X"),n-sum(t)))
        else:
            t.append(0)
            
    if sum(t) < n:
        return "Not enough!"
    return t if n>0 else "Game On"