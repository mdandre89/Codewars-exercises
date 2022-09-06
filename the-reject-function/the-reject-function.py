def reject(seq, predicate): 
    return list(filter(lambda x: not predicate(x), seq))