def land_perimeter(arr):
    a = "".join(arr)
    b_count = "".join(arr).count("X")*4   
    f = len(arr[0])
    for i,j in enumerate(a):
        if i < len(a)-f:
            if j == "X" and a[i+1]=="X" and (i+1)%(f)!=0:
                b_count-=2
            if j == "X" and a[i+f]=="X":
                b_count-=2
        elif i < len(a)-1 and (i+1)%(f)!=0:
            if j == "X" and a[i+1]=="X":
                b_count-=2
        else:
            pass      
    return 'Total land perimeter: '+ str(b_count)