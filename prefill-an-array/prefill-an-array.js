function prefill(n, v) {
  if(n%1!==0 || n<0 || isNaN(parseInt(n))){throw TypeError(n + " is invalid")}
  if(n==0){return []}
  return Array(n).fill(v || undefined)
}