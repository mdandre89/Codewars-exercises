const surface_area = function(A){
  let l = A.length
  let bottom_area = 0
  let horizontal_area = 0
  let vertical_area = 0
  
  for(let row of A){
    bottom_area+=row.filter(j=>j!=0).length
  }
  
  for(let row of A){
    for(let [index, element] of row.concat([0]).entries()){
      if(index === 0){
        horizontal_area += element
      }else{
        horizontal_area += Math.abs(element - row[index-1])
      }
    }
  }
  
  const trasposedA = A[0].map((col, i) => A.map(row => row[i]))
  for(let row of trasposedA){
    for(let [index, element] of row.concat([0]).entries()){
      if(index === 0){
        vertical_area += element
      }else{
        vertical_area += Math.abs(element - row[index-1])
      }
    }
  }
  
  return vertical_area + horizontal_area + 2*bottom_area
  
}