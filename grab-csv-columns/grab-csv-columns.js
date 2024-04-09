function csvColumns(csv, indices){
var c = csv.split("\n").map(a=>a.split(",").filter((a,i)=>indices.indexOf(i)!=-1).join(",")).filter(a=>a!="")
return c.length>0 ?csv.split("\n").map(a=>a.split(",").filter((a,i)=>indices.indexOf(i)!=-1).join(",")).join("\n"):""
}