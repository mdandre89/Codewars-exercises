function longestWord(stringOfWords){

  return stringOfWords.split(' ')
    .reduce(
      (a, b) => 
        a.length > b.length
          ? a
          : b
    );

}