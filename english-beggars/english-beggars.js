function beggars(values, n){
  if(n==0){return []}
  if(n>values.length){return values.concat((new Array(n-values.length).fill(0)))}
 var t = []
 for(var k = 0; k < n; k++){
 t.push(values.filter((a,i)=>(i)%n==k?a:0).reduce((a,b)=>a+b))}
 return t
}
//.reduce((a,b)=>a+b).map(a=>parseInt(a))