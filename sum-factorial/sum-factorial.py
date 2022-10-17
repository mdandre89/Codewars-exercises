def sum_factorial(lst):
    def fact(x):
        y=1
        for i in range(1,x+1):
            y=y*i
        return y   
    return sum([fact(j) for j in lst] )
   