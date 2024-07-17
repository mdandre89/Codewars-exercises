def min(arr):
    b=arr[0]
    for i in arr:
        if b>=i:
            b = i
        else:
            pass
    return b
            

def max(arr):
    b=arr[0]
    for i in arr:
        if b<=i:
            b = i
        else:
            pass
    return b