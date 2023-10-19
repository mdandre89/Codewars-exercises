import math
def new_avg(arr, newavg):
    if newavg*(len(arr)+1)-sum(arr) < 0:
        raise Exception("Error expected")
    return math.ceil(newavg*(len(arr)+1)-sum(arr))