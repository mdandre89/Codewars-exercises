function abacaba(n) {
var s="abcdefghijklmnopqrstuvwxyz";
while(!Number.isInteger(Math.log2(n))){
n = Math.pow(2, Math.floor(Math.log2(n))+1) - n
}
return s[Math.log2(n)]


}