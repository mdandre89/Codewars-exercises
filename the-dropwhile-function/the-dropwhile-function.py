def drop_while(arr, pred):
    try:
        return arr[list(map(lambda x: pred(x), arr)).index(False):]
    except:
        return []