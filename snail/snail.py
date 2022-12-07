def snail(array):
    t = []
    while array:
        t += array[0]
        del array[0]
        array = list(zip(*array))[::-1]
    return t