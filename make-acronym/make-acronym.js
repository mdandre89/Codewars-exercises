function toAcronym( input ){
  return input.split(" ").map((a) => a[0].toUpperCase()).join("");
}