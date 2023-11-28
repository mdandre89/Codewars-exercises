function validISBN10(isbn) {
  console.log()
  return isbn.split("").reduce((a,b,i)=>b=="X"?a+10*(i+1):a+b*(i+1),0)%11==0&&/\d{10}|\d{9}X/.test(isbn)
}