function invert(array) {
  return array.map(a => (a != 0) ? -a : 0);
}