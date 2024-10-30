function findEvenIndex(arr)
{
  for (var i = 0; i < arr.length; i ++) {
    if (arr.slice(0, i).reduce((a, b) => a + b, 0) == arr.slice(i + 1).reduce((a, b) => a + b, 0)) return i;
  }
  return -1;
}