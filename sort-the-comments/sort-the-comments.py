def sort_ranks(ls):
    M = max(i.count(".") for i in ls)
    ls = [(i +".0"*(M-i.count("."))).split(".") for i in ls ]
    ls2 = [".".join(j for j in i if j!=0) for i in sorted(ls, key=lambda x: list(map(int,x)))]
    return [i.replace(".0","") for i in ls2]