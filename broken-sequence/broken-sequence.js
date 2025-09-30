function findMissingNumber(sequence){
  if(sequence==""){return 0;};
  var t = sequence.split(" ").map(function(num){
  return parseInt(num);
});;
  var j = t.reduce(function(a,b){
  return a+b;
})
  if (isNaN(j)){return 1;}
  var n = Math.max(...t);
  for(var i=1;i<n;i++){
  if(t.indexOf(i)==-1){return i;};
  };
  return 0;
}