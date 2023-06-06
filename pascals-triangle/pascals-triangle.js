function pascalsTriangle(n) {
  if(n==1){return [1]}
  if(n==2){return [1,1,1]}
  var t = [[1], [1,1], [1,2,1]]
  for(var i = 3; i<n; i++){
  var k = t[i-1]
  var s =[]
  for(var j=0; j<k.length-1;j++){s.push(k[j]+k[j+1])}
  t.push([1].concat(s).concat([1]))}
  return [].concat.apply([], t);
}