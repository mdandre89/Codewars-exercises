function sepStr(arr) {
  var ls = arr.split(" ").map(a=>a.split(""))
  var t = []
  var maX = arr.split(" ").reduce((a,b)=>a.length>b.length?a:b).length
  for(var j=0;j<maX;j++){
  s = []
  for(var i=0; i<ls.length;i++){
  if(ls[i][j]){s.push(ls[i][j])}else{s.push("")}}
  t.push(s)}
  return t
}