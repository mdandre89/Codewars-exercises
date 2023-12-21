function atomicNumber(num){
  var s = 0;
  var i = 1;
  var t = []
  while(s<num){
  s +=(2*Math.pow(i, 2));
  if(s<num){
  t.push(2*Math.pow(i, 2));}else{
  t.push(t!="" ? num - t.reduce((a,b)=>a+b):num )
  }
  i++;
  }
  return t
}