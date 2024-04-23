function geometricSequenceElements(a, r, n){
  var t = []
  for(var i=0;i<n;i++){
  t.push(a)
  a = a*r
  }
  return t.join(", ")
}