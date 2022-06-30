import math

def yes_no(arr):
        ls, k, c = [], 0, 0
        while k < len(arr)*(math.log(max(len(arr),1), 2)+2):
                index = k%len(arr)
                if arr[index] != '':
                    if c%2 == 0:
                        ls.append(arr[index])
                        arr[index] = ''
                    c+=1
                k+=1 
        return ls