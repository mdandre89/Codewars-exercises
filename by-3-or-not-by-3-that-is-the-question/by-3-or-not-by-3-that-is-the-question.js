function divisibleByThree(str){
return str.split("").reduce((a,b)=>a+parseInt(b),0)%3 == 0
}