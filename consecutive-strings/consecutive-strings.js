function longestConsec(strarr, k) {
    if(k*strarr.length<=0||strarr.length<k){return ""}
    var t = []
    var strarr2 = strarr.map(a=>a.length)
    for(var i=0; i+k<=strarr.length;i++){
    t.push(strarr2.slice(i,i+k).reduce((a,b)=>a+b))    
    }
    var inde = t.indexOf(Math.max(...t))
    return strarr.slice(inde,inde+k).join("")
}