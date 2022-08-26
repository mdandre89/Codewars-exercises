function isSolved(board) {
 var board1 = board.map(a=>a.join("")).join("-")
 var test = board1.match(/([12])\d{2}-\1\d{2}-\1\d{2}|\d([12])\d-\d\1\d-\d\1\d|\d{2}([12])-\d{2}\1-\d{2}\1/)
 if(test){return parseInt(test[1])}
 var test2 = board1.match(/([12])\1{2}/)
 if(test2){return parseInt(test2[1])}
 var test3 = board1.match(/([12])\d{2}-\d\1\d-\d{2}\1|d{2}([12])-\d\2\d-\d\d\2/)
 if(test3){return parseInt(test3[1])}
 return board1.indexOf("0")==-1?0:-1
}