def sort_by_binary_ones (num_list): 
    return sorted(num_list, key=lambda x: (-bin(x).count('1'), len(bin(x)), x))