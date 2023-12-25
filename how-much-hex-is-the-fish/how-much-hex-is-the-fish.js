function fisHex(name) {
  name = name.toLowerCase()
  if(name==""){return 0}
  s ="abcdef"
  t = []
  for(var i =0; i<name.length; i++){
  if (s.indexOf(name[i])!=-1){t.push(parseInt(name[i],16))}
  }
  return t.reduce(function(a,b){return a^b})
}