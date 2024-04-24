const mapPopulationFit = (population, fitness) => {
  var t = []
  for(var i=0;i<population.length;i++){
  t.push( {"chromosome":population[i],"fitness":fitness(population[i])} )
  }
  return t
}