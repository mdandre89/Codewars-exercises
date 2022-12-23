function distributionOf(ls){
  let beg = [0,0]
  let j=0
  while(ls.length>0){
     beg[j%2] += (ls[0]>=ls[ls.length -1]? ls.shift():ls.pop())
     j+=1}
  return beg
} 