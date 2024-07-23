function Xbonacci(signature,n){
 var l = signature.length
 var t = signature
 var i = l;
 while(i<n){
 t.push(t.slice(i-l,i).reduce(function(a,b){return a+b}))
 i++
 }
 return t.slice(0,n)
}