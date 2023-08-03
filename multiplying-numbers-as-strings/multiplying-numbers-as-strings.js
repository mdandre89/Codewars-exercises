function multiply(m, n){
  var t = [];
  m = m.replace(/^0+/,'').split("").reverse().join("");
  n = n.replace(/^0+/,'').split("").reverse().join("");
  var r = '';
  var s = 0;
  for(var i=0; i<m.length; i++){
  r = new Array(i+1).join('0');
  for(var j=0; j<n.length; j++){
  r += (( parseInt(n[j]) * parseInt(m[i]) + s)%10);
  s = Math.floor(( parseInt(n[j]) * parseInt(m[i])+s)/10);}
  r = r + s
  s = 0
  r = r.split('').reverse().join('');
  t.push(r);}
  s = sum(...t).replace(/^0+/,'')
  return s==[]?'0':s;
}

function sum(...args){
var t = args.reduce((t,a)=>suma(a,t),"0").replace(/\b0+/g, '');
return t == "" ? "0" : t;
}

function suma(a, b) {
  a = a.split("").reverse().join("");
  b = b.split("").reverse().join("");
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
  return r==0?s.split("").reverse().join(""):(s+r).split("").reverse().join("")
}