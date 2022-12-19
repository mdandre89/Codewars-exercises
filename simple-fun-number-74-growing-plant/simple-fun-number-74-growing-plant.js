function growingPlant(up, down, desiredHeight) {
  if(up>desiredHeight){return 1}
  var x = (desiredHeight-up)/(up-down)
  return x-Math.floor(x)>0 ?  Math.floor(x)+2 : Math.floor(x)+1
}