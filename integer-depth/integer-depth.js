function computeDepth (x){
  var s = new Set([x.toString().split("")]);
  var i = 1;
  while(Array.from(s).length<=10){
  s = new Set([...s, ...new Set((x*i).toString().split(""))]);
  i++;}
  return i-1;
}