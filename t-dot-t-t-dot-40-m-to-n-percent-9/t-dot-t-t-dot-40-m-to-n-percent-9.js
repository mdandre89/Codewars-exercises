function nMod9(m,n){
  let t = 0
  for(let i=m; i<=n; i++){
    t+=i
    t%=9
  }
  return t
}