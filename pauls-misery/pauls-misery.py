def paul(x):
    dictio = {"kata":5, "Petes kata":10, "life":0, "eating":1}
    tot = 0
    for i in x:
        tot += dictio[i]
    if tot < 40:
        return 'Super happy!'
    elif tot < 70:
        return 'Happy!'
    elif tot < 100:
        return 'Sad!'
    else:
        return 'Miserable!'