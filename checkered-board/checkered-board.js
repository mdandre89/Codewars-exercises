function checkeredBoard(d) {
if(d<2||typeof d!= 'number'||parseInt(d)!=d){return false}
var t = []
for(var j=0; j<d; j++){
t.push((new Array(d+1)).join(' ').split('').map((a,i)=>(i+j+d+1)%2==0?'■':'□').join(' '))}
return t.join('\n')
}