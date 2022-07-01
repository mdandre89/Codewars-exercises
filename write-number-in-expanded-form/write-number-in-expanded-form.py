def expanded_form(num):
    num = str(num)
    t = []
    for i,j in enumerate(num):
        if int(j) > 0:
            t.append(j + "0"*(len(num) -i-1))
    return " + ".join(t)