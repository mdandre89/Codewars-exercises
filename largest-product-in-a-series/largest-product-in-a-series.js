function greatestProduct(input) {
  var m = input.substr(0,5).split('').reduce((a,b)=>parseInt(a)*parseInt(b),1)
  for(var i=1;i+5<=input.length;i++){
  var l = input.substr(i,5).split('').reduce((a,b)=>parseInt(a)*parseInt(b),1)
  if(l>m){m=l}}
  return m
}