function bmi(weight, height) {
  var p = weight/Math.pow(height,2);
  if(p<=18.5){return "Underweight"}
  if(p<=25.0){return "Normal"}
  if(p<=30.0){return "Overweight"}
  return "Obese";
}