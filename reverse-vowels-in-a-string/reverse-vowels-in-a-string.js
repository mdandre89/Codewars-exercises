function reverseVowels(str) {
if(!str.match(/[aeiouAEIOU]/gi)){return str}
var ls = str.match(/[aeiouAEIOU]/gi).reverse()
str = str.split("")
j = 0
for(var i=0;i<str.length;i++){
if("aeiouAEIOU".indexOf(str[i])!=-1){
str[i] =ls[j];
j++}}
return str.join("")
}