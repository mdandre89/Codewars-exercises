function findUniq(arr) {
var result={};
for(var i=0; i<arr.length; i++){
  if(!result[arr[i]])
        result[arr[i]] = 0;
    ++result[arr[i]];
}
for(var j in result){
if(result[j]==1){return Number(j)}
}
}