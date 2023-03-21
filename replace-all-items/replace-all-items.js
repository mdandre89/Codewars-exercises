function replaceAll(seq, find, replace) {
var al;
typeof seq=="string"? al=seq.split("") : al=seq
al.forEach((el,ind,arr)=>el==find?arr[ind]=replace: el)
return typeof seq=="string"? al.join("") : al
}