def take_while(arr, pred_fun):
    try:
        return arr[0: list(map(lambda x: pred_fun(x), arr)).index(False)]
    except:
        return arr