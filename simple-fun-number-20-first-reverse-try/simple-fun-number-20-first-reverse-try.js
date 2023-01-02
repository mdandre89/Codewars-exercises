function firstReverseTry(arr) {
  if (arr.length <=1){return arr;} 
  var t = [arr[arr.length - 1]].concat(arr.slice(1,-1)).concat([arr[0]]);
  return t;
}