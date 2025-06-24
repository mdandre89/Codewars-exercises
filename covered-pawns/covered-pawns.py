def covered_pawns(pawns):
    safe = len(pawns)
    for i in pawns:
        if not (set.intersection(area(i),set(pawns))):
            safe -=1
    return safe
    
def area(i):
    st  = "0abcdefgh0"    
    a = st[st.index(i[0])-1]+str(int(i[1])-1)
    b = st[st.index(i[0])+1]+str(int(i[1])-1)
    return {a,b}