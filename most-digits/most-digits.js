function findLongest(array){
var maxi = array[0]
array.forEach((a)=>String(a).length> String(maxi).length? maxi=a:maxi)
return maxi
}