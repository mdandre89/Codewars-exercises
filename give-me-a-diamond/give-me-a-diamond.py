def diamond(n):
    if n==0 or n==2 or n<0:
        return None
    t = []
    for i in range(1,n+1,2):
        if i ==1:
            t.append(" "*max((n-1)/2,0) +"*"*i+ "\n")
        else:
            t.append(" "*max((n-i)/2,0) +"*"*i+ "\n")
    return "".join(t[0:-1]) + t[-1] + "".join(t[0:-1][::-1]) 