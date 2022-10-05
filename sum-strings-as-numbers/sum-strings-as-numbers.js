function sumStrings(a, b) {
  a = a.split("").reverse().join("")
  b = b.split("").reverse().join("")
  var s = "";
  var r = 0;
  var t = 0;
  for(var i=0;i<Math.max(a.length,b.length);i++){
  if(a[i] && b[i]){t = parseInt(a[i]) + parseInt(b[i]) + r}
  else if(a[i]){t = parseInt(a[i]) + r}
  else if(b[i]){t = parseInt(b[i]) + r}
  r = Math.floor(t/10)
  s += t-r*10
  }
  return r==0?s.split("").reverse().join("").match(/[^0]\d*/)[0]:(s+r).split("").reverse().join("").match(/[^0]\d*/)[0]
}