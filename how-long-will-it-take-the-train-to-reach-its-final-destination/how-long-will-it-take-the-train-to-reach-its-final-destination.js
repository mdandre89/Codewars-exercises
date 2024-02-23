function reachDestination(distance, speed) {
var value = Math.round(distance/speed * 1.0/0.5)*0.5;
return value==1? "The train will be there in " + value + " hour." :"The train will be there in " + value+ " hours."
}