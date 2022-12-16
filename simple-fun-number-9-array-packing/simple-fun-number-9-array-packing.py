def array_packing(arr):
    return int("".join([("00000000"+bin(i)[2:])[-8:] for i in arr][::-1]),2) if len(arr) >0 else 0