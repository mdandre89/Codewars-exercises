function f(n, m) {
  return m*(m-1)/2 * Math.floor(n/m) + ((n%m)*((n%m)+1))/2;
}