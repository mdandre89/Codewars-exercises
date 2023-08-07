def multiple(x):
    n = bool(x%5)
    m = bool(x%3)
    dictio = {(0,0):"BangBoom",(1,0):"Boom",(0,1):"Bang"}
    return dictio.get((m,n), "Miss")