def shuffled_array(s):
    s.remove(sum(s)/2)
    return sorted(s)