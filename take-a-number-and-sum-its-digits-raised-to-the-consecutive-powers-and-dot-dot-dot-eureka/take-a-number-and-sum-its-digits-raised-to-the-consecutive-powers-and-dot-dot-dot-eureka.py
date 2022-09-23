def sum_dig_pow(a, b):     
    return filter(lambda x: x ==sum([int(j)**(i+1) for i,j in enumerate(str(x))]), range(a,b+1))