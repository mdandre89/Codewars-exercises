def find_in_array(seq, predicate): 
    for index, item in enumerate(seq):
        if predicate(item, index):
            return index
    return -1