function max(array) {
  if(array.length === 0){
    return -Infinity
  }
  if(array.length === 1){
    return array[0]
  }else if(array.length === 2){
    return array[1] > array[0] ? array[1] : array[0]
  }else{
    const partialMax = max(array.slice(1))
    return array[0] > partialMax ? array[0] : partialMax
  }
}