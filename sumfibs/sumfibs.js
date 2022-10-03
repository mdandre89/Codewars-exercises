function sumFibs(n) {
  var s = 0;
  var a = 1;
  var b = 1;
  var t = 0;
  for(var i = 0; i<n-1;i++){
  t = a;
  a = b;
  b = b+t;
  if(a%2==0){s+=a}}
  return s
};