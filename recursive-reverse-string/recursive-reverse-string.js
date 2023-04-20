function reverse(stri) {
    if(stri.length<=1){return stri}
        
    return reverse(stri.substr(1)) + stri[0] 
}