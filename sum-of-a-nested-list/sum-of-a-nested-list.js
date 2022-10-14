const sumNested = arr => {
return arr.reduce((a,b)=> b instanceof Array? a+sumNested(b):a+b,0)
};