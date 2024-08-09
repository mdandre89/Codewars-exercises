def even_fib(m):
    s = 0
    i = 1
    while fibo(i)<m:
        if fibo(i)%2==0:
            s+= fibo(i)
        i+=1  
    return s
    
    
def fibo(n,dictio={0:0,1:1}):
    if n in dictio:    
        return dictio[n]
    else:
        dictio[n] = dictio[n-1] + dictio[n-2]
        return dictio[n]