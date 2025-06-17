function cycle(dir, arr, cur) {
  if(arr.indexOf(cur)==-1){return null}
  return arr.indexOf(cur)+dir>=0?arr[(arr.indexOf(cur)+dir)%arr.length]:arr[arr.length-1]
  
}