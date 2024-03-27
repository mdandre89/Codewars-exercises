function stockList(listOfArt, listOfCat){
  if(listOfArt=="" || listOfCat==""){return ""}
  return listOfCat.map(a=>"("+a+" : "+counta(listOfArt,a)+")").join(" - ")
}

function counta(lista,st){
var rex = new RegExp("^"+st); 
return lista.reduce((a,b)=> rex.test(b)?a+parseInt(b.match(/\d+/g)):a,0)
}