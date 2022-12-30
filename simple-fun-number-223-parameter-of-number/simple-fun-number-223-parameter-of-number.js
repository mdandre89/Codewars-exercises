function parameter(n) {
var m = n.toString().split("").reduce((a,b)=>a*b,1)
var s = n.toString().split("").reduce((a,b)=>parseInt(a)+parseInt(b),0)
  return m*s/gcd(m,s)
}

var gcd = function(a, b) {
    if ( ! b) {return a;}
    return gcd(b, a % b);};