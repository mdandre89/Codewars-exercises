def evaporator(co, ev, th):
    rem = co
    y = 0
    while rem > th/100*co:
        rem = rem*(1-ev/100)
        y+=1
    return y