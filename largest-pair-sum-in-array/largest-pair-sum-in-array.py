def largest_pair_sum(numbers): 
    ls = sorted(numbers, reverse=True)
    return ls[0] + ls[1]