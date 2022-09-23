function sumDigPow(a, b) {
var t = []
for(var i=a; i<b+1;i++){if(sump(i)==i){t.push(i)}}
return t
}

function sump(m){
return m.toString().split("").map((a,i)=>Math.pow(parseInt(a),i+1)).reduce((a,b)=>a+b,0)
}