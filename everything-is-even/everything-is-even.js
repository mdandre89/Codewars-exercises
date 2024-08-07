function ensureEven(n) {
return n>=0? Math.floor(n)%2+Math.floor(n):-(Math.floor(-n)%2+Math.floor(-n))
}