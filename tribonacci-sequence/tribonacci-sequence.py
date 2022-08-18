def tribonacci(si,n):
    j = 0
    while len(si)<n:
        si.append(sum(si[j:j+3]))        
        j+=1
    return si[0:n]