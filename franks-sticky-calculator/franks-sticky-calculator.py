def sticky_calc(operation, val1, val2):
    val1 = str(round(val1)) + str(round(val2))
    val2 = str(round(val2))
    return round(eval(val1 +operation +  val2))
    