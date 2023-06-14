const dc = {"G":1, "KG":1000, "T":1000000}
const trasf = (a)=> /\d+/.exec(a)*dc[/[A-Z]+/.exec(a)[0]]

const arrange=(arr)=> arr.sort((a,b)=>trasf(a)>trasf(b))