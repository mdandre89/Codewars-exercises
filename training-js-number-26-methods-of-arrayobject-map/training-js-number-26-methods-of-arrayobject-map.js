function isolateIt(arr){
return arr.map(a=> a.length%2==0? a.slice(0,a.length/2)+"|"+a.slice(a.length/2,a.length):a.slice(0,a.length/2)+"|"+a.slice(a.length/2+1,a.length))
}