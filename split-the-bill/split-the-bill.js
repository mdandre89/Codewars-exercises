function splitTheBill(x) {
 var s=0;
 var i=0;
 for(var key in x) {
    s+=x[key];
    i+=1
}  
s = s/i;
 for(var key in x) {
    x[key]=parseFloat((x[key]-s).toFixed(2));
    i+=1} 
return x;
}