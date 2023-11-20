function jumble(strin){
  return strin.replace(/\w*/gi, function(s){
if(s.length>3){return s[0]+s[s.length-2]+s.substr(1,s.length-3)+s[s.length-1];}
else{return s;}
})
}