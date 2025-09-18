function reverseCase(strin) {
return strin.replace(/((\w)\2{1,})/g,f)
}

function f(s){
if(s==s.toUpperCase()){return s.toLowerCase()}
if(s==s.toLowerCase()){return s.toUpperCase()}
return s
}