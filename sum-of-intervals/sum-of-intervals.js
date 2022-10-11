function sumIntervals(intervals){
var news = intervals.sort((a,b)=>a[0]>= b[0] && a[1]>= b[1])
var s = [];
for(var j = 0; j<news.length; j++){
  if(s == ''){
  s.push(news[j])}
  else{ var t = s.splice(-1, 1);
      if(t[0][1] >= news[j][0]){      
          if(t[0][1] <= news[j][1]){var newt = [t[0][0],news[j][1]]; s.push(newt)}
          else{ var newt = [t[0][0],t[0][1]];  s.push(newt)  }}
      else{s.push(t[0]);s.push(news[j])}
 }
}
return s.reduce((a,b)=>a+b[1]- b[0],0)
}