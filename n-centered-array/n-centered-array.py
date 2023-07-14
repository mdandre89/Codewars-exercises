def is_centered(arr,n):
    l = len(arr)
    print(arr,n)
    print(arr[l//2-2:l//2+2])
    if n == 0  and( l%2 ==0 or l==1):
        return True
    return any(sum(arr[l//2-i:l//2+i+1])==n for i in range(0,l)) if l%2==1 else any(sum(arr[l//2-i:l//2+i])==n for i in range(0,l//2+1))