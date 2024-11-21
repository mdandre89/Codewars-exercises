function dirReduc(arr){
  let s = arr.join("-")
  let i =0;
  while(i<Math.floor(arr.length/2)){
  s = s.replace(/NORTH-SOUTH|SOUTH-NORTH|EAST-WEST|WEST-EAST/g,"").replace(/--/,"-").replace(/^-|-$/,"")
  i+=1}
  return s!==""? s.split("-") : []
}