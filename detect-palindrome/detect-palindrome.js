function isPalindrome(str){
  str = str.toLowerCase();
  str = str.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"");
  str = str.replace(/\s/g,"");
  console.log(str);
  for(var i = 0; i < str.length; i++){
    if(str.charAt(i) !== str.charAt(str.length-i-1)){
      return false;}  }
  return true;
}