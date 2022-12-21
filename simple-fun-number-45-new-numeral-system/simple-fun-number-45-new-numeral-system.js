function newNumeralSystem(number) {
 var al ="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
 var t = [];
 var n = al.indexOf(number);
 var m;
 if(n%2!=1){m=n/2+1;}else{m=n/2}
for(var i=0; i<m;i++){
t.push(al[i] +" + "+ al[n-i]);
};
  
  return t;
}