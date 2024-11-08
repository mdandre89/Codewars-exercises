def get_a_down_arrow_of(n):   
    if n < 1:
        return ""
    t = []
    for i in range(1,n+1):
        t.append((i-1)*" " + "".join(str(i%10) for i in range(1,n-i+1)) + str((n-i+1)%10) + "".join(str(i%10) for i in range(1,n-i+1))[::-1])
    return "\n".join(t)      
    