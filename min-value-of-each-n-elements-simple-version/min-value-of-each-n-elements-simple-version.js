function minValue(arr,n){
  var t = []
  for(var i=0; i+n<=arr.length;i++){
  t.push(arr.slice(i,i+n).reduce((a,b)=>a<b?a:b))}
  return t
}