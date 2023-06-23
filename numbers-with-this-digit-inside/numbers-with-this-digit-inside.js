function numbersWithDigitInside(x, d) {
  var t=[]; 
  for(var i=1;i<=x;i++){
  if(i.toString().indexOf(d.toString())!=-1){t.push(i)}
  }
  if(t==""){return [0,0,0]}
  return  [t.length,t.reduce((a,b)=>a+b),t.reduce((a,b)=>a*b)] 
}