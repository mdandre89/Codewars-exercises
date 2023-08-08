def my_crib(n):
    r = ""
    for i in range(n):
        r+= " "*(n-i) + "/" + " "*2*i + "\\" + " "*(n-i) + "\n"
    
    r += "/" + "_"*2*n + "\\" +"\n"
    
    for i in range(n-1):
        r += "|"  +" "*2*n+"|" +"\n"
        
    r += "|"  +"_"*2*n+"|"
    
    return r