def the_biggest_search_keys(*tre):
    if not tre:
        return "''" 
    s = [i for i in tre if len(i)==max([len(i) for i in tre])]
    return "'"+"', '".join(sorted(s)) +"'" 