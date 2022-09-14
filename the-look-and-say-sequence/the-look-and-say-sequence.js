function getLines(n){
  if(n<=0 || isNaN(n)){return -1}
  var t = ["1"];
  for(var i = 1; i<n; i++){
  t.push(t[i-1].replace(/((\d)\2*)/g,function(a,b,c){return a.length +c}));
  }
  return t.join(",");
}