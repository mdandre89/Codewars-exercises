def divisible_by_last(n):
    itera = iter(list('0' + str(n)))
    ls = []
    for value in str(n):
        preceding = int(next(itera))
        if preceding == 0 or int(value)%preceding:
            ls.append(False)
        else:
            ls.append(True)
    return ls