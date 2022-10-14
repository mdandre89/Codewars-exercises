function findSum(n) {
 var i = Math.floor(n/5);
 var j = Math.floor(n/3);
 var z = Math.floor(n/15);
 return 5*(i*(i+1)/2) + 3*(j*(j+1)/2)  - 15*(z*(z+1)/2);
}