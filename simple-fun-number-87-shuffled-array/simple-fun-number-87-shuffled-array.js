function shuffledArray(shuffled) {
  var s = shuffled.reduce(function(a,b){return a+b});
  shuffled.splice(shuffled.indexOf(s/2),1);
  return shuffled.sort(function(a, b){return a-b});;
}