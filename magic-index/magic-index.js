// return the magic index
function findMagic(arr){
  let s = -1
  for(let i=0; i<arr.length; i++){
    if(i === arr[i]){
      s = i
      break
    }
  }
  return s
}