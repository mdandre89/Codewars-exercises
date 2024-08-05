function balance(left,right){
  var l = 2*(left.match(/\!/g)||[]).length +3*(left.match(/\?/g)||[]).length
  var r = 2*(right.match(/\!/g)||[]).length +3*(right.match(/\?/g)||[]).length
  if(l == r){return "Balance"}
  return r>l ?"Right":"Left"
}