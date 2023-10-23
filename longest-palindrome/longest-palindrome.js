longestPalindrome=function(s){
var M = 0;
for(var i=0; i < s.length; i++){
for(var j=0; i+ j <= s.length; j++){
var v = s.substr(i,j);
var revMyArr = v.split("").reverse().join("");
if (v == revMyArr && v.length>M){M = v.length};}}
return M 
}