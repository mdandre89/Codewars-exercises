function noBoringZeros(n) {
  return n!=0 ? parseInt(n.toString().replace(/0*$/,"")) : 0
}