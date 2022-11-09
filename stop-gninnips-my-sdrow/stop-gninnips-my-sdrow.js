function spinWords(strin){
  return strin.replace(/\w*/gi, function(s){
if(s.length>4){return s.split("").reverse().join("");}
else{return s;}
})



}