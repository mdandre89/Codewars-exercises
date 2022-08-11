function getTwoComplementInt(n) {
if(n==0){return 2}
return Math.ceil(Math.log2(n))!=Math.log2(n) ? Math.pow(2,Math.ceil(Math.log2(n)))-n:n
}