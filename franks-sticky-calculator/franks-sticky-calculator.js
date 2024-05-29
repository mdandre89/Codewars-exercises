function stickyCalc (operation, val1, val2){
    val1 = String(Math.round(val1)) + String(Math.round(val2))
    val2 = String(Math.round(val2))
    return Math.round(eval(val1 +operation +  val2))
}