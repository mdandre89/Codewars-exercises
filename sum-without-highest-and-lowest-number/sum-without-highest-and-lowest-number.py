def sum_array(arr):
    if arr == 0 or arr == None or arr==[] or len(arr)==1:
        return 0
    else:
        return sum(list(arr)) -max(arr)- min(arr) if len(arr) >1 else arr