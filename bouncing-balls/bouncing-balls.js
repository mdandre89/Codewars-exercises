function bouncingBall(h,  bounce,  window) {
if( h < 0 || bounce>=1 || bounce<=0 || window>h || window<=0){return -1}
var y = 0
    while(h > window){
        h = h * bounce
        y += 1}
return 2*(y-1)+1
}