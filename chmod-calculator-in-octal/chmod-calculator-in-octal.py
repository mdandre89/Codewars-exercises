d = {'r':4, 'w':2, 'x':1}
def chmod_calculator(perm):
    return '{}{}{}'.format(
        sum(d.get(i,0) for i in perm.get("user",'-') ),
        sum(d.get(i,0) for i in perm.get("group",'-') ),
        sum(d.get(i,0) for i in perm.get("other",'-') )
    ) if perm!={} else "000"