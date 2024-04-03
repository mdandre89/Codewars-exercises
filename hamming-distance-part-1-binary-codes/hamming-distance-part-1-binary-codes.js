function hammingDistance(x,y){
  return x.split("").reduce((a,b,i)=>b!=y[i]?a+1:a ,0)
}