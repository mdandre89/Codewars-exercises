def board(inp):
    return ["".join([ret(i,k,z) for k,z in enumerate(j)]) for i,j in enumerate(inp)]
    
def ret(i,j,s):
    if s in {"+","-","|","*"}:
        return s
    t = sum(1 for m in range(j-1,j+2) for l in range(i-1,i+2) if inp[l][m] == "*")
    return str(t) if t else " "