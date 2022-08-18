function tribonacci(si,n){
 var j = 0
 while(si.length<n){
 si.push(si.slice(j,j+3).reduce((a,b)=>a+b,0))
 j+=1}
 return si.slice(0,n)
}