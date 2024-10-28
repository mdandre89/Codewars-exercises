def even_binary(n):
    array = n.split(" ")
    filtered_array = filter(lambda x: (x[-1] == '0'), array)
    sorted_array = sorted(filtered_array, key=lambda x: int(x, 2))
    
    i = 0 
    s = ''
    for item in array:
        if item[-1] == '0':
            s += sorted_array[i] + ' '
            i+=1 
        else:
            s += item + ' '
    return s.strip()