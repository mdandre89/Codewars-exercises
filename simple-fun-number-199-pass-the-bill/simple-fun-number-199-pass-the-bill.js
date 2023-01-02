function passTheBill(n, m, k) {
  if (m<k&&n-m-k+m<k){return -1;}
  for(var i=0; i<=n-m-k; i++){if(i+m>n-m-i){return i;}}
  return -1;
}