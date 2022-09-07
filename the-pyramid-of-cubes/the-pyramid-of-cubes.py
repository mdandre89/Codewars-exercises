def find_height(cubes):
    n = 0 
    while (n*(n+1)*(n+2)/6 - cubes) <= 0:
        n+=1
        
    return n - 1 