function reverseLetter(str) {
  return str.match(/[a-z]/gi).reverse().join('')
}