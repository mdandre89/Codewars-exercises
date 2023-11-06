def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays:
        return 0
    for subarray in array_of_arrays:
        if not subarray:
            return 0

    min_l = min(array_of_arrays, key=len)
    max_l = max(array_of_arrays, key=len)
    return sum(range(len(min_l), len(max_l) +1)) - sum(len(subarr) for subarr in array_of_arrays)