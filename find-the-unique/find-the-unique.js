function findUniq(arr) {
let [a,b]  = new Set(arr)
return arr.slice(0,3).reduce((c,d)=>d==a?c+1:c,0)==1?a:b
}