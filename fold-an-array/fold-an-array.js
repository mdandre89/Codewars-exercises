function foldArray(arr, runs){

for(var i=0;i<runs;i++){arr = fold(arr)}
return arr
}

function fold(ar){
var l = ar.length;
var t = [];
if (l%2==1){ for(j=0;j<Math.floor(l/2);j++){t.push(ar[j] + ar[l-j-1])}
t.push(ar[Math.floor(l/2)]);
return t;
}
else{for(j=0;j<l/2;j++){t.push(ar[j] + ar[l-j-1])}return t}
}