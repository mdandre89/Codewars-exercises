function wave(stri){
var t =[]
  for(i=0;i<stri.length;i++){
  if(stri[i]!=" ")
  t.push(stri.substr(0,i) +stri[i].toUpperCase()+ stri.substr(i+1,stri.length) )
  }
  return t
}