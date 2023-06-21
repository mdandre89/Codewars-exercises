def shake_tree(tree):
    ls = [1 if i == "o" else 0 for i in tree[0]]
    for i in tree[1:]:
        ls = change(ls,i)
    return ls  
    
def change(l, pattern):
    for i,j in enumerate(pattern):
        if j == "_" and l[i]>0:
            l[i] = 0
        elif j == "/" and l[i]>0:
            try:
                l[i-1] += l[i]
            except:
                pass
            l[i] = 0            
        elif j == "\\" and l[i]>0 :
            try:
                l[i+1] += l[i]
            except:
                pass
            l[i] = 0  
    return l