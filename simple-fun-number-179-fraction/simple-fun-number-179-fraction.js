function fraction(a, b) {
function gdc(a,b){return !b? a:gdc(b,a%b)}
return a/gdc(a,b)+b/gdc(a,b)
}