var gimme = function (inputArray) {
  var newA = inputArray.slice().sort((a,b)=> a-b)
  return inputArray.indexOf(newA[1])
};