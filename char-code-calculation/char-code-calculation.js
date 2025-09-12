function calc(x){
 var a = x.split('').map(b=>b.charCodeAt().toString()).join('')
return 6*a.split('').reduce((a,b)=>a+(b==7?1:0),0)
}