def isOddHeavy(arr):
    try:
        m = min(filter(lambda x: x%2==1,arr))
    except:
        return False
    try:
        n = max(filter(lambda x: x%2==0,arr))
    except:
        return True
    return m>n