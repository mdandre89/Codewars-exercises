function subtract(a, b){
  var M = Math.max(a.length,b.length)
  a = new Array(M-a.length).join("0") + a,b = new Array(M-b.length).join("0") + b //So I can compare the 2 numbers
  if(b>a){return  "-" + subtract(b,a)}
  a = a.split("").reverse(),  b = b.split("").reverse();
  var result = "";
  for(var i=0;i<M;i++){
    a[i] = a[i] || "0", b[i] = b[i] || "0"
    if(a[i]<b[i]){a[i+1] = (parseInt(a[i+1]) -1).toString();
          result += (10+ parseInt(a[i]) - parseInt(b[i])).toString();}
    else{result += (parseInt(a[i]) - parseInt(b[i])).toString()} }
  result = result.split("").reverse().join("").replace(/^0+/,"")
  return result == "" ? "0": result}