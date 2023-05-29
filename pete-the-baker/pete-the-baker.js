function cakes(recipe,available) {
  t = []
  for(var item in recipe){
  if(!available.hasOwnProperty(item)){t.push(0)}else{
  t.push(Math.floor(available[item]/recipe[item]))}
  }
  return t.reduce((a,b)=>Math.min(a,b))
}