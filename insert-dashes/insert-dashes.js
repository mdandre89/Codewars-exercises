function insertDash(num){
   return num.toString().replace(/[13579]{2,}/g,myfunc)
}

function myfunc(n){
return n.toString().split("").join("-")
}