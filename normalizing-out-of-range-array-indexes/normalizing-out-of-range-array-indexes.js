function normIndex(array, index){
  var l = array.length
return index>0 ? array[index%l] : array[(l+(index%l))%l]
}