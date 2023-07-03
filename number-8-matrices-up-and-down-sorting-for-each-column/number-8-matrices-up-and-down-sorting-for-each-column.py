def up_down_col_sort(matrix):
    m = len(matrix)
    n = len(matrix[0])
    flat_list = sorted(x for xs in matrix for x in xs)
    ls = []
    for i in range(n):
        if i%2 ==0:
            ls.append(flat_list[i*m:(i+1)*m])
        else:
            ls.append(flat_list[i*m:(i+1)*m][::-1])
    return [list(i) for i in [*zip(*ls)]]