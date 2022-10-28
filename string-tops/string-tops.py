def tops(msg):
    s = 1
    i = 2
    t = []
    while s <= len(msg):
        if i%2 == 0:
            t.append(msg[s])
        s += i
        i += 1         
    return "".join(t[::-1])