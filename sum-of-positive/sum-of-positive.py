def positive_sum(arr):
    if len(arr)>0:
        return sum([item for item in arr if item>0])
    else:
        return 0