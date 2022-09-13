def sequence(n):
    lst=[0,1,1,2]
    lst1=[0,2,2,1]
    n = n-1
    if (n//4)%2==1:
        return lst1[n%4]
    if (n//4)%2==0:
        return lst[n%4]
    return n%4