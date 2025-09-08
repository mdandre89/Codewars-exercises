function chessBoardCellColor(cell1, cell2) {
var leto= "ABCDEFGH";
if((leto.indexOf(cell1[0])-leto.indexOf(cell2[0])+parseInt(cell1[1])-parseInt(cell2[1]) )%2){return false}
return true
}