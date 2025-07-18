function closeCompare(a, b, margin){
  if (Math.abs(a-b)<=margin || a===b){return 0}else{return Math.abs(a-b)/(a-b);}
}