def solve(s):
    t = 0
    for i in range(1,len(s)+1):
        for j in range(i+1):
            if s[j:i] and int(s[j:i])%2==1:
                t+=1            
    return t