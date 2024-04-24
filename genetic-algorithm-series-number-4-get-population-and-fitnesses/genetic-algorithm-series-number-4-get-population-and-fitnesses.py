def mapPopulationFit(population, fitness):
    return [ChromosomeWrap(chromosome=i, fitness=fitness(i)) for i in population]