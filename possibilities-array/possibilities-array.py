def is_all_possibilities(arr):
    return len(arr) and set(range(len(arr))).issubset(arr)