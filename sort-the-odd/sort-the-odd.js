function sortArray(array) {
  var dis = array.filter(a=>a%2==1)
  var dis = dis.sort((a,b)=>a-b)
  var z = 0;
  var t = []
  for(var i = 0;i<array.length;i++){
  if(array[i]%2==1){t.push(dis[z])
  z+=1}
  else{t.push(array[i])}
  }
  return t
}