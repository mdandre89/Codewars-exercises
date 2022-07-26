def tickets(people):
    dictio = {25:0,50:0,100:0}
    for i in people:
        if (i==50 and dictio[25]==0) or (i==100 and dictio[50]==0 and dictio[25]<3) or (i==100 and dictio[50]>=1 and dictio[25]==0):
            return "NO"
        dictio[i] +=1
        if i == 50:
            dictio[25] -= 1
        if i == 100 and (dictio[25]>=3 or dictio[50]>=1 and dictio[25]>=1):
            if dictio[50]>=1 and dictio[25]>=1:
                dictio[50] -= 1
                dictio[25] -= 1
            elif dictio[25]>=3:
                dictio[25] -= 3
    return "YES"