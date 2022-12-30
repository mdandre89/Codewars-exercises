def array_center(arr):
    return list(filter(lambda x: abs(x-sum(arr)/len(arr))<min(arr),arr))