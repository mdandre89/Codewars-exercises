function scramble(str1, str2) {
var st2  = Array.from(new Set(str2.split(""))).join("")
for(var i = 0; i<st2.length; i++){
if((str2.match(new RegExp(st2[i], 'g'))||[]).length>(str1.match(new RegExp(st2[i],'g'))||[]).length){return false}
}
return true
}