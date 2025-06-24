function coveredPawns(pawns){
    var st  = "0abcdefgh0"
    return pawns.filter(a=>pawns.indexOf(st[st.indexOf(a[0])-1]+((a[1])-1))!=-1||pawns.indexOf(st[st.indexOf(a[0])+1]+((a[1])-1))!=-1).length;}