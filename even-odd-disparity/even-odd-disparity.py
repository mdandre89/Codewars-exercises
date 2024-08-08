def solve(a):
    s = [i for i in a if type(i)==int and i%2==0]
    return len([i for i in a if type(i)==int and i%2==0]) - len([i for i in a if type(i)==int and i%2==1])