def fibonacci(n, dictio={1:1, 0:0}):
    if n in dictio:
        return dictio[n]
    else:
        dictio[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dictio[n]