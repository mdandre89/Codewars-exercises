function convertHashToArray(hash){
  var t = []
  for(var item in hash){
  t.push([item,hash[item]])
  }
  return t.sort()
}