function getMissingIngredients(recipe, added) {
if(Object.keys(added).length === 0){return recipe}
var m = cakes(recipe,added)
var miss={}
for(var i in recipe){
if(m*recipe[i]-(added[i]!==undefined? added[i]:"")!=0){miss[i] = m*recipe[i] - (added[i]!==undefined? added[i]:"")}}
return miss
}

function cakes(recipe,available) {
  t = []
  for(var item in recipe){
  if(!available.hasOwnProperty(item)){t.push(0)}else{
  t.push(Math.ceil(available[item]/recipe[item]))}
  }
  return t.reduce((a,b)=>Math.max(a,b))
}