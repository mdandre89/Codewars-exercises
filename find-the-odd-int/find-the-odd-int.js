function findOdd(A) {
for(var i=0; A.length; i++){
if( A.reduce(function(n, val){return n + (val === A[i]);}, 0) % 2 == 1){return A[i]}}
}