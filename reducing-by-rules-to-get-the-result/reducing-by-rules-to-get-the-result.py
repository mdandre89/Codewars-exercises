import functools
def reduce_by_rules(lst, rules):
    return functools.reduce(lambda i,x:rules[(x[0]+1)%len(rules)](i,x[1]),enumerate(lst[2:]),rules[0](lst[0],lst[1]))