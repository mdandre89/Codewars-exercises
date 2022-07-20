function whatCentury(year){
var y = year%100==0?year/100:Math.floor(year/100)+1
if(y%10==1 &&(y>20||y<10)){return y+'st'}
if(y%10==2 &&(y>20||y<10)){return y+'nd'}
if(y%10==3 &&(y>20||y<10)){return y+'rd'}
return y+'th'
}