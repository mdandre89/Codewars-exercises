def luck_check(n):   
    if n == "":
        raise ValueError
    try:    
        n = [int(i) for i in str(n)]
        return sum(n[:len(n)/2]) ==  sum(n[len(n)/2:]) if len(n) % 2 == 0 else sum(n[:(len(n)-1)/2]) ==  sum(n[(len(n)-1)/2+1:])
    except:
        raise ValueError 