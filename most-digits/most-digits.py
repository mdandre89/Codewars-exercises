def find_longest(arr):
    maxi = arr[0]
    for i in arr:
        if len(str(i))>len(str(maxi)):
            maxi=i          
    return maxi