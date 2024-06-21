function flattenAndSort(arr) {
 return arr!=""?arr.reduce((prev, curr)=>prev.concat(curr)).sort((a,b)=>a-b):[]
}