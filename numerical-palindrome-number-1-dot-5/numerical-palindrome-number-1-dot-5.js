function palindrome(num,s) { 
    if( typeof num !="number" || num<0 || typeof s !="number"){return 'Not valid'}       
    var t = [] ;
    var i=1;
    while(i<=s){
        if(pali(num)){t.push(num);
            i+=1;}
        num+=1;}
    return t;
    
function pali(n){
    if (n>10 && n.toString()==n.toString().split("").reverse().join("")){ return true}
    return false}

}