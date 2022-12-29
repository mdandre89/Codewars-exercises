function compareIntegers(a, b) {
  if(a.length>b.length|| b.length>a.length){return a.length>b.length? "greater" : "less"}  
  for(i=0;i<a.length;i++){
  if(a[i]>b[i]){return "greater"}else if(b[i]>a[i]){return "less"}  }
  return "equal"
}