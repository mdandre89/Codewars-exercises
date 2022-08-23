function touchType(s) {
  var lh = '12345qwertasdfgzxcvb'
  var res = ''
  for(var i=0; i<s.length;i++){
  if(s[i]==' '){if(i==0){ res+='L'}else if(lh.indexOf(s[i-1])!=-1){res+="R"}else{res+="L"}}
  else if(lh.indexOf(s[i])!=-1){ res+="L"}
  else{ res+="R"}
  }
  return res;
}