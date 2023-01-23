function calculator(a,b,sign){
if("+-/*".indexOf(sign)!=-1 && parseFloat(a) && parseFloat(b)){
return eval(a+sign+b)} else {return "unknown value"}

}