def sort_array(arr):
    dis = sorted([i for i in arr if i%2==1])
    z = 0
    for i,j in enumerate(arr):
        if j%2 == 1:
            arr[i] = dis[z]
            z+=1
    return arr