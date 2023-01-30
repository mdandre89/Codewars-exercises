def sequence_classifier(arr):
    starting=arr[0]
    ending=arr[-1]
    previous=starting
    si=0
    sd=0
    co=0
    l=len(arr)
    for i in arr[1:]:
        if i<previous:
            sd+=1
        elif i>previous:
            si+=1
        elif i==previous:
            co+=1
        previous=i

    if co == l-1:
        return 5
    if sd==l-1:
        return 3
    if co and si+co==l-1: 
        return 2
    if co and sd+co==l-1:
        return 4
    if si == l-1:
        return 1
    return 0
    
    
    