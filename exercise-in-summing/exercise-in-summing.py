def minimum_sum(values, n):
    if n == 0 or not values:
        return 0
        
    return sum(sorted(values)[:n]) if n <=len(values) else sum(values) 

def maximum_sum(values, n):
    if n == 0 or not values:
        return 0
    return sum(sorted(values)[::-1][:n]) if n <=len(values) else sum(values) 