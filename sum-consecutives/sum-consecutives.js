function sumConsecutives(s) {
  var t = [s[0]];
  var j=0;
  var i=0;
  while(i<s.length-1){
  if(s[i]==s[i+1]){
  t[j] +=s[i];
  }else{j=j+1;
  t[j]=s[i+1]}  
  i++;}
  return t;
}