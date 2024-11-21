def dirReduc(arr):
    l  = len(arr)
    opp = {"NORTH":"SOUTH", "SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    j = 0 
    while j < l/2:
        for i in range(max(len(arr)-1,0)):
            if i+1<len(arr) and arr[i] == opp[arr[i+1]]:
                arr = arr[:i] + arr[i+2:]
        j += 1
    return arr