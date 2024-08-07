function evil(n) {
    var t = n.toString(2).match(/1/g||[]).length
    return t%2 == 0 ?  "It's Evil!" : "It's Odious!"
}