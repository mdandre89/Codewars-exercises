function isPangram(strng){
  strng = strng.toLowerCase()
  var s = "abcdeifghilmnopqrstuvzwxkj"
  for(var i=0;i<26;i++){
  if(strng.indexOf(s[i])==-1){return false;}
  }
  return true;
}