function elementsSum(arr,d=0){
return arr2 = arr.reduce((a,b,i)=>calc(b,i,arr.length,d)+a,0)
}

function calc(a,i,l,d){
return a.length>l-i-1?a[l-i-1]:d
}