function perfectSquare(s){
  n = s.split('\n').length
  ls = new Array(n+1).join('.')
  ar = new Array(n).join(ls+"\n")+ls
  return s==ar
}