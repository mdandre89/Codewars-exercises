function gcd_rec(a, b) {
    if(b){return gcd_rec(b, a % b)}
    else{return Math.abs(a)}}

function mnLCM(m,n) {
  var lst = [];
for (var i = Math.min(n,m); i <= Math.max(n,m); i++){lst.push(i)}
console.log(lst)
  return lst.reduce( function(a,b){return a*b/gcd_rec(a,b) } ) 
}