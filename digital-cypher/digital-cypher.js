function encode(str,  n){
  var m = n.toString();
  var t = str.split("").map((a,i)=>a.charCodeAt(0)-96+Number(m[i%m.length]));
  return t
}