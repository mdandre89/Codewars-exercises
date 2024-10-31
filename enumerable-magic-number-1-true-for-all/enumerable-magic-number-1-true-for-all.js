function all( arr, fun ){
  return arr.filter(a=> fun(a)).length==arr.length
}