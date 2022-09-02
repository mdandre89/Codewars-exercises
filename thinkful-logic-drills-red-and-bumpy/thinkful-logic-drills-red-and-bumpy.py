dictio = {"bumpy":{"green":1,"yellow":2,"red":4},"smooth":{"green":1,"yellow":1,"red":1}}
def color_probability(c, t):
    return str( dictio[t][c]/sum(dictio[t].values()) )[:4] 