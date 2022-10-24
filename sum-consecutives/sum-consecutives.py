def sum_consecutives(s):
    t = [s[0]]
    j = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            t[j] +=s[i]
        else:
            j +=1
            t.append(s[i+1]) 
    return t