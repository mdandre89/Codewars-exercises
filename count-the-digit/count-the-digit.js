function nbDig(n, d) {
    var s = 0;
    var d1 = new RegExp(d,"gi")
    for(var i=0; i<=n; i++){
    s += ( (i*i).toString().match(d1) || [] ).length
    }
    return s
}