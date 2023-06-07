def partlist(arr):
    return [(" ".join(arr[:j])," ".join(arr[j:])) for j in range(1,len(arr))]