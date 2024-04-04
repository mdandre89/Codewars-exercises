def group_by_commas(n):
    return "".join([j+"," if i%3==0 and i>1 else j for i,j in enumerate(str(n)[::-1])][::-1])