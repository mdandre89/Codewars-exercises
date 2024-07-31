function remove(s){
var n = (s.match(/!/g) || []).length
  return  s.replace(/!/g,"") + new Array(n+1).join("!") 
  }