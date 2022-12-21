function areSimilar(A, B) {
if(A.reduce(function(a,b){return a+b;})!=B.reduce(function(x,y){return x+y;})){return false;}
  var t=[];
  for(var i=0; i<A.length; i++){if(A[i]!=B[i]){t.push(i);}
  }
  
  if(t.length>2){return false;}else{return true;}
}