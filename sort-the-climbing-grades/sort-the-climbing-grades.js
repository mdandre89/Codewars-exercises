function sortGrades(ls){
let d = ["VB",'V0','V0+','V1','V2','V3','V4','V5',"V6",'V7','V8','V9','V10','V11','V12','V13',
"V14",'V15', 'V16', 'V17']
return ls.sort((a,b)=>d.indexOf(a)-d.indexOf(b))
}