function isOddHeavy(n){
  var odd = n.filter(a=>a & 1)
  var even = n.filter(a=>!(a & 1))
  return n!="" && (even=="" || odd!="" && odd.reduce((a,b)=>a>b?b:a) > even.reduce((a,b)=>a>b?a:b)) ? true : false
}