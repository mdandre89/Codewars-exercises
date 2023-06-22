function palindrome(num) {
if(typeof num !== "number"||num<0){return "Not valid"}
var num = num.toString();
function pali(num){
if( num.length==2 && num[0]==num[1] || num.length==1){return true}
if( num[num.length-1]==num[0] ){return pali(num.substring(1,num.length-1))}
return false
}
return pali(num)
} 