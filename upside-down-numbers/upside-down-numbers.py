dictio = {"0":"0","1":"1","6":"9","9":"6","8":"8"}
def solve(a, b):
    y = 0
    for i in range(int(a),int(b)):
        if transf(i):
            y+=1
    return y

def transf(n):
    n = str(n)
    for i,j in enumerate(n):
        if j not in dictio:
            return False
        elif dictio[j] != n[-i-1]:
            return False
    return True