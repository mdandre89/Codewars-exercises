def consecutive(arr, a, b):
    for index, item in enumerate(arr[0:-1]):
        if item == a:
            if arr[index+1] == b:
                return True
        if item == b:
            if arr[index+1] == a:
                return True
            
    return False