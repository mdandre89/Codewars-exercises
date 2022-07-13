def cookie(x):
    if isinstance(x,str):
        return 'Who ate the last cookie? It was Zach!'
    return 'Who ate the last cookie? It was Monica!' if type(x) ==float or type(x) == int else  "Who ate the last cookie? It was the dog!"