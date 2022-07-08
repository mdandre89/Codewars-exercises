def will_fit(present, box): 
    return [ i + 2 <= j for i,j in zip(sorted(present), sorted(box)) ].count(False) == 0