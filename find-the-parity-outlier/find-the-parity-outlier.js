function findOutlier(integers){
return integers.map(l=>l%2?0:1).reduce((a,b)=>a+(b===1),0)>1?integers[integers.map(l=>l%2?0:1).indexOf(0)]:integers[integers.map(l=>l%2?0:1).indexOf(1)]
}