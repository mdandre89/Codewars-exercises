function scoreOfDive(scores, tariff) {
  return Math.round(scores.sort( (a, b) => a - b).slice(2, -2).reduce((partialSum, a) => partialSum + a, 0)*tariff * 100) / 100
}