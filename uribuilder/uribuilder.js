class UriBuilder {
  constructor(root) {
    this.root = root;
    this.params = {};
  }
  
  build(){
    let ls = []
    for (const [key, value] of Object.entries(this.params)) {
      ls.push(`${key}=${encodeURI(value)}`)
    }
    url = ls.join('&')
    if(ls.length == 0){
      return this.root
    }else{
      let baseroot = this.root.split('?')[0]
      return baseroot + '?' + url
    }
  }
}