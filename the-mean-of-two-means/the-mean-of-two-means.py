    
def get_mean(arr,x,y):
    def mean(numbers):
        return float(sum(numbers)) / max(len(numbers), 1)
    
    if 1 < x <= len(arr) and 1 < y <= len(arr):
        return mean([mean(arr[0:x]),mean(arr[-y:])])
    else:
        return -1