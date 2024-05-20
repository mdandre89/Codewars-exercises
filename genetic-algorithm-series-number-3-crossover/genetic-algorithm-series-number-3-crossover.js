const crossover = (chr1, chr2, indexx) => {
return [chr1.slice(0,indexx).concat(chr2.slice(indexx)),chr2.slice(0,indexx).concat(chr1.slice(indexx))] 
};