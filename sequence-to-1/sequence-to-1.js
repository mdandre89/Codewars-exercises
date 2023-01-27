function seqToOne(n){
if(n>=0){return n>0?Array.from(Array(n+1).keys()).reverse().slice(0,n):[0,1]}else{
return seqToOne(-n).map(a=>-a).concat([0,1])
}
} 