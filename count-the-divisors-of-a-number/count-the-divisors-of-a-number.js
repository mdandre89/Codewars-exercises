function getDivisorsCnt(n){
   var s = 0
   for(var i=0; i<=n; i++){
   if(n%i==0){s+=1}
   }
   return s
}