function maxDiff(list) {
  if(list.length==0){return 0;}
  var m = Math.min(...list);
  var M = Math.max(...list);
  return M-m;
};