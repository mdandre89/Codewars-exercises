function myFirstKata(a,b) {
console.log(a,b)
  if (typeof(a)=="number" && typeof(b)=="number" ){return a%b + b % a;} 
  else {
    return false;
  }
}