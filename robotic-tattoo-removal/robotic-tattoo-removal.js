function robot(skinScan) {
    return skinScan.map(a=>a.join("-").replace(/X/g,"*").split("-"))
}