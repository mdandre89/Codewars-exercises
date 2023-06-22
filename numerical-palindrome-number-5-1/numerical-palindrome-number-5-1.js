function palindrome(num) {
  if(typeof num != 'number'|| num<=0){return "Not valid"}
  var s = Array.from(new Set(num.toString().split('')));
  var dis = 0
  for(var i=0;i<s.length;i++){
  if(num.toString().match(new RegExp(s[i],'g')).length%2==1){dis+=1}}
  return dis>=2||num.toString().length==1?false:true
}