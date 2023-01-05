function gHappy(strng) {
if(strng.replace(/g{2,}/g).indexOf("g")==-1){return true}
return false 
}