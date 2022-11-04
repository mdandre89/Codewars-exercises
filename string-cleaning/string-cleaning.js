function stringClean(s){
 return s.match(/[^0-9]/gi) !=null? s.match(/[^0-9]/gi).join(""): ""
}