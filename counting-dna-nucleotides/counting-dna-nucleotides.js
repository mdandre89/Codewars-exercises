function getCountedNucleotides(genCode){
  let dictio = {A:0,C:0,G:0,T:0}
  for(let i=0; i<genCode.length; i++){
    const letter = genCode[i].toUpperCase()
    if(letter in dictio){
      dictio[letter] += 1 
    }
  }
  return dictio
}