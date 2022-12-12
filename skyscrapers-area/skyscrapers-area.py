def surface_area(A):
    l= len(A)
    bottom_area = sum([sum([1 for j in row if j!=0]) for row in A])
    top_area = bottom_area
    
    horizontal_area = sum([sum([value if counter == 0 else abs(value - row[counter-1]) for counter, value in enumerate(row+ [0])]) for row in A])
    vertical_area = sum([sum([value if counter == 0 else abs(value - row[counter-1]) for counter, value in enumerate(row+ [0])]) for row in [list(i) for i in zip(*A)]])
    
    return top_area + bottom_area + horizontal_area + vertical_area