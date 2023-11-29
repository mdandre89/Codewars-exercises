function isVow(a){
return a.map(i=>[97,101,105,111,117].indexOf(i)!=-1?  String.fromCharCode(i) :i)
}