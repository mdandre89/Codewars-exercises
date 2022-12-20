function crossingSum(matrix, a, b) {
return matrix[a].reduce( (a,b)=>a+b ) + matrix.map( i=>i==matrix[a]?0:i[b]).reduce((a,b)=>a+b)
}