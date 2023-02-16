def rgb(r, g, b):
    s = ""
    for i in [r,g,b]:
        if 0<i<=255:
            s += hex(i)[2:] if i>10 else "0"+hex(i)[2:]
        elif i>255:
            s += "FF"
        else:
            s += "00"
    return s.upper()