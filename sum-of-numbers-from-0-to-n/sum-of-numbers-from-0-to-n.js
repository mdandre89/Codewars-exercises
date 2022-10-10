var SequenceSum = (function() {
  function SequenceSum() {}

  SequenceSum.showSequence = function(count) {
  if(count==0){return "0=0";}
  else if(count<0){return count+"<0";} 
var n = new Array(count).fill(0);
n = n.map(function(a,b){return a+b+1})
return "0+"+n.join("+") + " = "+ n.reduce(function(a,b){return a+b})
  };
  return SequenceSum;
})();