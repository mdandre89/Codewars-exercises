function printerError(s) {
    return (s.match(/[nopqrstuvzxyw]/gi)||[]).length + "/"+s.length
    
}